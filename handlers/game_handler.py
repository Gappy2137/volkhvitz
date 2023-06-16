"""Game handler."""
from imports import *

enemy_list = []

enemy_dict = {
    "red_fairy": [FairyRed(), enemy_list],
    "blue_fairy": [FairyBlue(), enemy_list]
}


def create_enemy(x, y, enemy_type):
    enemy = enemy_dict[enemy_type][0]
    enemy.x, enemy.y = x, y
    enemy_list.append(enemy)
    return enemy
