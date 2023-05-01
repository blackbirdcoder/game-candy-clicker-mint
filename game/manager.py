import pygame as pg
from random import sample
import pickle
from config import SENSOR_SIZE, LEVEL_COUNTER_LIMIT, REWARDS, DEFAULT_REWARD, RECORD_FILE_NAME, WINDOW, PROPORTION


class Manager:
    __sensor_mask = None
    __hit = False
    __level_counter = 0
    __level_counter_limit = LEVEL_COUNTER_LIMIT
    __rewards = REWARDS
    __default_reward = DEFAULT_REWARD
    __score = None
    __level = None
    __record = 0
    __num_prize = 2
    __filename = RECORD_FILE_NAME + '.pickle'

    def __init__(self, score, level):
        self.__score = score
        self.__level = level

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
        if self.__level > 5:
            self.__num_prize = 3
        self.__score += 1
        reward = self.__default_reward
        self.__level_counter += 1
        if self.__level_counter == self.__level_counter_limit:
            self.__level_counter = 0
            self.__level += 1
            reward = ''.join(sample(self.__rewards, self.__num_prize))
        self.__default_reward = reward
        return self.__score, self.__level, reward

    def get_default_reward(self):
        return self.__default_reward

    def record_check(self):
        try:
            with open(self.__filename, 'rb') as f:
                self.__record = pickle.load(f)
                return self.__record
        except FileNotFoundError as error:
            with open(self.__filename, 'wb') as f:
                pickle.dump(self.__score, f)
                return self.__score

    def record_save(self, score):
        with open(self.__filename, 'rb') as f:
            last_record = pickle.load(f)
        if last_record < score:
            with open(self.__filename, 'wb') as f:
                pickle.dump(score, f)

    @staticmethod
    def birth(screen, targets, speed, live_targets):
        for target in targets:
            surface, positions = target
            pos_x, pos_y = positions[0:2]
            pos_y += speed
            live_targets.append(screen.blit(surface, (pos_x, pos_y)))

    @staticmethod
    def delete(live_targets, targets, idx):
        del live_targets[idx]
        del targets[idx]

    @staticmethod
    def border_crossing(live_targets, targets, delete):
        for idx, current_live_target in enumerate(live_targets):
            if current_live_target[1] > WINDOW['HEIGHT'] - PROPORTION * 2:
                delete(live_targets, targets, idx)
