from imports import *

bullet_list = []


def calc_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    rads = math.atan2(-dy, dx)
    rads %= 2 * math.pi
    return rads
