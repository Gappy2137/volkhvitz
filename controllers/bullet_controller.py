from imports import *

bullet_list = []
bullet_remove_list = []


def calc_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    rads = math.atan2(-dy, dx)
    rads %= 2 * math.pi
    return rads


def calc_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx ** 2 + dy ** 2)
    return distance


def calc_angle_spd(x1, y1, x2, y2, speed):
    dx = x2 - x1
    dy = y2 - y1
    rads = math.atan2(-dy, dx)
    rads %= 2 * math.pi

    rads_final = rads + math.asin(speed / calc_distance(x1, y1, x2, y2))

    return rads_final