from imports import *

enemy_list = []

spawn_x = 192
spawn_y = -32
top = -16
middle = 224
bottom_uwu = 544
pos_x = [24, 24 + 32, 24 + (32 * 2), 24 + (32 * 3), 24 + (32 * 4), 24 + (32 * 5), 24 + (32 * 6), 24 + (32 * 7), 24 + (32 * 8), 24 + (32 * 9), 24 + (32 * 10)]
mid_x = 168
fly_left = -64
fly_right = BARS_RIGHT + 64

enemy_path = {
    "group_none": [2137],
    "group_1": [(pos_x[1], top),
                (pos_x[1], middle),
                (fly_left, bottom_uwu)],
    "group_2": [(pos_x[9], top),
                (mid_x, middle),
                (fly_right, bottom_uwu)]
}
