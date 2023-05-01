import pygame as pg
from random import randrange
from config import WINDOW, PROPORTION, TARGET_SIZE, MAX_TARGETS, LEVEL_UP


class Target:
    __max_targets = MAX_TARGETS
    __start = 0
    __quantity = 3  # no more than __max_targets
    __position_x = []
    __limit = WINDOW['WIDTH'] - TARGET_SIZE[0]
    __step = PROPORTION * 3 + 15
    __targets = []
    __size = PROPORTION
    __level_up = LEVEL_UP

    def __init__(self, surface, target):
        self.surface = surface
        self.target = target

    def create_mask(self):
        return pg.mask.from_surface(self.target)

    def _random_position_x(self):
        while len(self.__position_x) < self.__quantity:
            rand_num = randrange(self.__start, self.__limit, self.__step)
            if rand_num not in self.__position_x:
                self.__position_x.append(rand_num)

    def _quantity_increase(self):
        if self.__quantity < self.__max_targets:
            self.__quantity += 1
            print(self.__quantity)
        else:
            raise Exception(f'Limit reached. Limit {self.__max_targets}')

    def create_targets(self):
        self._random_position_x()
        for num in range(len(self.__position_x)):
            self.__targets.append(
                (self.target, (self.__position_x[num], self.__size * randrange(0, 3), self.__size, self.__size))
            )
        self.__position_x = []

    def get_targets(self):
        if len(self.__targets) > 0:
            return self.__targets
        else:
            raise Exception('Target list is empty')

    def respawn(self):
        self.create_targets()
        return self.get_targets()

    def increase_targets(self, level):
        if level in self.__level_up:
            self._quantity_increase()
            del self.__level_up[0]
