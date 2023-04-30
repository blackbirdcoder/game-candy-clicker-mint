import pygame as pg
from random import choice
from config import SENSOR_SIZE, LEVEL_COUNTER_LIMIT


class Manager:
    __sensor_mask = None
    __hit = False
    __level_counter = 0
    __level_counter_limit = LEVEL_COUNTER_LIMIT
    __rewards = ['(+-+)', '(0_0)', '(*=*)']
    __default_reward = '(*-*)'
    __score = None
    __level = None
    __record = None

    def __init__(self, score, level, record):
        self.__score = score
        self.__level = level
        self.__record = record

    def init_hit_sensor(self):
        sensor = pg.Surface(SENSOR_SIZE)
        self.__sensor_mask = pg.mask.from_surface(sensor)

    def check_hit(self, target_mask, offset):
        if self.__hit:
            self.__hit = False

        if self.__sensor_mask is not None:
            if target_mask.overlap(self.__sensor_mask, offset):
                self.__hit = True
        else:
            raise Exception('No sensor initialization')
        return self.__hit

    def calculate_progress(self):
        self.__score += 1
        reward = self.__default_reward
        self.__level_counter += 1
        if self.__level_counter == self.__level_counter_limit:
            self.__level_counter = 0
            self.__level += 1
            reward = choice(self.__rewards)
            self.__default_reward = reward
        return self.__score, self.__level, reward,

    def get_default_reward(self):
        return self.__default_reward

