import os
import sys
import pygame as pg
from ui import Panel, Text, Cursor
from target import Target
from manager import Manager
from config import WINDOW, FPS, COLORS, GAME_NAME, FONT_SIZE, TARGET_SIZE, FONT_REWARD_SIZE


def main():
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((WINDOW['WIDTH'], WINDOW['HEIGHT']))
    pg.display.set_caption(GAME_NAME)
    screen.fill(COLORS['MAIN_SPACE'])
    click_sfx = pg.mixer.Sound(os.path.join('assets', 'click.mp3'))
    background = pg.image.load(os.path.join('assets', 'background.jpeg'))
    background = pg.transform.scale(background, (WINDOW['WIDTH'], WINDOW['HEIGHT']))
    font = pg.font.Font(os.path.join('assets', 'KosugiMaru-Regular.ttf'), FONT_SIZE)
    font_candy = pg.font.Font(os.path.join('assets', 'Candy-icons.ttf'), FONT_REWARD_SIZE)
    hand_cursor = pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND)
    arrow_cursor = pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW)
    candy = pg.image.load(os.path.join('assets', 'candy.png')).convert_alpha()
    candy = pg.transform.scale(candy, TARGET_SIZE)
    target = Target(screen, candy)
    target_mask = target.create_mask()
    score, level = 0, 0
    manager = Manager(score, level)
    record = manager.record_check()
    manager.init_hit_sensor()
    reward = manager.get_default_reward()
    move_speed = 0
    targets = []
    speed_number = manager.get_speed_number()

    while True:
        screen.blit(background, (0, 0))
        live_targets = []
        mouse_pos = pg.mouse.get_pos()
        move_speed += speed_number

        if len(targets) == 0:
            move_speed = speed_number
            targets = target.respawn()

        manager.birth(screen, targets, move_speed, live_targets)
        manager.border_crossing(live_targets, targets, manager.delete)
        if target.increase_targets(level):
            speed_number += manager.speed_up()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                manager.record_save(score)
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for idx, current_target in enumerate(live_targets):
                        offset = (mouse_pos[0] - current_target[0]), (mouse_pos[1] - current_target[1])
                        if manager.check_hit(target_mask, offset):
                            click_sfx.play()
                            progress = manager.calculate_progress()
                            score, level, reward = progress
                            manager.delete(live_targets, targets, idx)

        position_names = ['top', 'bottom']
        Panel(screen, position_names).create()

        notification_templates = [f'score:{score}', f'record:{record}', f'level:{level}', 'reward: ']
        Text(screen, font, notification_templates).display_notification()
        notification_reward = reward
        Text(screen, font_candy, notification_reward).display_reward()

        Cursor(hand_cursor, arrow_cursor).switching()

        pg.display.update()
        clock.tick(FPS)
        pg.display.flip()


if __name__ == '__main__':
    main()
