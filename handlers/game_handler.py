"""Game handler."""
from imports import *


def create_enemy(x, y, enemy_type, waypoints, pattern, freq, change_pattern):
    enemy = enemy_type
    enemy.x, enemy.y = x, y
    enemy.current_frame = random.randint(0, 3)
    enemy.waypoints = waypoints
    enemy.bullet_pattern = pattern
    enemy.bullet_freq = freq
    enemy.bullet_set_freq()
    enemy.change_pattern = change_pattern
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
