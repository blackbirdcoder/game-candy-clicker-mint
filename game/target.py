from random import randrange
from config import WINDOW, PROPORTION, TARGET_SIZE, MAX_TARGETS


class Target:
    __max_targets = MAX_TARGETS
    __start = 0
    __quantity = 3  # no more than __max_targets
    __position = []
    __limit = WINDOW['WIDTH'] - TARGET_SIZE[0]
    __step = PROPORTION * 3 + 15
    __targets = []
    __size = PROPORTION

    def __init__(self, surface, target):
        self.surface = surface
        self.target = target

    def _random_position(self):
        while len(self.__position) < self.__quantity:
            rand_num = randrange(self.__start, self.__limit, self.__step)
            if rand_num not in self.__position:
                self.__position.append(rand_num)

    def quantity_increase(self):
        if self.__quantity < self.__max_targets:
            self.__quantity += 1
        else:
            raise Exception(f'Limit reached. Limit {self.__max_targets}')

    def create_targets(self):
        self._random_position()
        for num in range(len(self.__position)):
            self.__targets.append(
                self.surface.blit(
                    self.target, (self.__position[num], self.__size, self.__size, self.__size)
                )
            )

    def get_targets(self):
        if len(self.__targets) > 0:
            return self.__targets
        else:
            raise Exception('Target list is empty')
