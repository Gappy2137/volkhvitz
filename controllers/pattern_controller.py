"""Pattern controller."""

from imports import *


class EnemyPattern1:
    x: int
    y: int
    spd: int

    def __init__(self, x, y, spd):
        self.x = x
        self.y = y
        self.spd = spd

    def make_move(self):
        self.y += self.spd
        return self.y
