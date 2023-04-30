from enum import Enum
import pygame as pg
from config import COLORS, PROPORTION, WINDOW


class Panel:
    class Name(Enum):
        top = 0
        bottom = 1

    __panel_name = Name
    __color = COLORS['PANEL']
    __size = PROPORTION

    def __init__(self, surface, position_names):
        self.surface = surface
        self.position_names = position_names

    def create(self):
        for position in self.position_names:
            if position == self.__panel_name.top.name:
                rect = pg.Rect(0, 0, self.surface.get_width(), self.__size)
                panel = pg.draw.rect(self.surface, self.__color, rect)
            elif position == self.__panel_name.bottom.name:
                rect = pg.Rect(0, (self.surface.get_height() - self.__size), self.surface.get_width(), self.__size)
                panel = pg.draw.rect(self.surface, self.__color, rect)
            else:
                raise Exception('Panel cannot be created. Panel name does not match')


class Text:
    __positioning = [
        (PROPORTION * 2, 7),
        (WINDOW['WIDTH'] - PROPORTION * 5, 7),
        (PROPORTION * 2, WINDOW['HEIGHT'] - PROPORTION + 7),
        (WINDOW['WIDTH'] - PROPORTION * 5, WINDOW['HEIGHT'] - PROPORTION + 7),
        (WINDOW['WIDTH'] - 100, WINDOW['HEIGHT'] - 40),
    ]
    __color = COLORS['TEXT']

    def __init__(self, surface, font, notifications):
        self.surface = surface
        self.font = font
        self.notifications = notifications

    def display_notification(self):
        for idx, position in enumerate(self.__positioning[0:4]):
            item = self.notifications[idx]
            ui_text = self.font.render(item.upper(), True, self.__color)
            self.surface.blit(ui_text, position)

    def display_reward(self):
        pos = self.__positioning[-1]
        item = self.notifications
        reward_text = self.font.render(item, True, self.__color)
        self.surface.blit(reward_text, pos)


class Cursor:
    __size = PROPORTION
    __aria = WINDOW['HEIGHT'] - PROPORTION

    def __init__(self, active, passive):
        self.active = active
        self.passive = passive

    def switching(self):
        cursor_pos_y = pg.mouse.get_pos()[1]
        if cursor_pos_y >= self.__size and cursor_pos_y < self.__aria:
            pg.mouse.set_cursor(self.active)
        else:
            pg.mouse.set_cursor(self.passive)
