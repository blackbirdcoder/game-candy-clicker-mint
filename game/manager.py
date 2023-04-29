import pygame as pg
from config import SENSOR_SIZE


class Manager:
    __sensor_mask = None

    @classmethod
    def init_hit_sensor(cls):
        sensor = pg.Surface(SENSOR_SIZE)
        cls.__sensor_mask = pg.mask.from_surface(sensor)

    @classmethod
    def check_hit(cls, target_mask, offset):
        if cls.__sensor_mask is not None:
            if target_mask.overlap(cls.__sensor_mask, offset):
                pass
        else:
            raise Exception('No sensor initialization')
