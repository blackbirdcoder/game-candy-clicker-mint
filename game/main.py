import sys
import pygame as pg
from config import WINDOW, FPS, COLORS, GAME_NAME


def main():
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((WINDOW['WIDTH'], WINDOW['HEIGHT']))
    screen.fill(COLORS['MAIN_SPACE'])
    pg.display.set_caption(GAME_NAME)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        clock.tick(FPS)
        pg.display.flip()


if __name__ == '__main__':
    main()