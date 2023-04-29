import os
import sys
import pygame as pg
from ui import Panel, Text, Cursor
from target import Target
from manager import Manager
from config import WINDOW, FPS, COLORS, GAME_NAME, FONT_SIZE, TARGET_SIZE


def main():
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((WINDOW['WIDTH'], WINDOW['HEIGHT']))
    pg.display.set_caption(GAME_NAME)
    screen.fill(COLORS['MAIN_SPACE'])
    background = pg.image.load(os.path.join('assets', 'background.jpeg'))
    background = pg.transform.scale(background, (WINDOW['WIDTH'], WINDOW['HEIGHT']))
    font = pg.font.Font(os.path.join('assets', 'KosugiMaru-Regular.ttf'), FONT_SIZE)
    hand_cursor = pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND)
    arrow_cursor = pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW)
    candy = pg.image.load(os.path.join('assets', 'candy.png')).convert_alpha()
    candy = pg.transform.scale(candy, TARGET_SIZE)
    target = Target(screen, candy)
    target_mask = target.create_mask()
    Manager.init_hit_sensor()
    screen.blit(background, (0, 0))
    target.create_targets()
    targets = target.get_targets()
    score, record, level = 0, 0, 0
    reward = '(*-*)'

    while True:
        mouse_pos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for current_target in targets:
                        offset = (mouse_pos[0] - current_target[0]), (mouse_pos[1] - current_target[1])
                        Manager.check_hit(target_mask, offset)

        position_names = ['top', 'bottom']
        Panel(screen, position_names).create()

        notification_templates = [f'score:{score}', f'record:{record}', f'level:{level}', f'reward:{reward}']
        Text(screen, font, notification_templates).display_notification()

        Cursor(hand_cursor, arrow_cursor).switching()

        pg.display.update()
        clock.tick(FPS)
        pg.display.flip()


if __name__ == '__main__':
    main()
