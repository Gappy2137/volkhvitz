"""Game handler."""
from imports import *


"""
enemy_dict = {
    "red_fairy": [FairyRed(), enemy_list],
    "blue_fairy": [FairyBlue(), enemy_list]
}
"""


def create_enemy(x, y, enemy_type):
    enemy = enemy_type
    enemy.x, enemy.y = x, y
    enemy.current_frame = random.randint(0, 3)
    enemy_list.append(enemy)
    return enemy


def create_fx(x, y, hsp, vsp, angle, fx_type, fx_behaviour, anim_spd):
    fx = Effect()
    fx.x, fx.y = x, y
    fx.hsp, fx.vsp = hsp, vsp
    fx.type = fx_type
    fx.behaviour = fx_behaviour
    fx.angle = angle
    fx.anim_spd = anim_spd
    fx_list.append(fx)
    fx.set_init_frame()
    return fx
