import os
import sys
import pygame as pg
from ui import Panel
from config import WINDOW, FPS, COLORS, GAME_NAME


def main():
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((WINDOW['WIDTH'], WINDOW['HEIGHT']))
    pg.display.set_caption(GAME_NAME)
    screen.fill(COLORS['MAIN_SPACE'])
    background = pg.image.load(os.path.join('assets', 'background.jpeg'))
    background = pg.transform.scale(background, (WINDOW['WIDTH'], WINDOW['HEIGHT']))
    screen.blit(background, (0, 0))

    for position in ['top', 'bottom']:
        Panel(screen, position).create()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        clock.tick(FPS)
        pg.display.flip()


if __name__ == '__main__':
    main()