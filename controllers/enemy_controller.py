from imports import *

enemy_list = []

spawn_x = 192
spawn_y = -64
top = -32
middle = 224
bottom_uwu = 544
pos_x = [24]
for i in range(1, 10):
    pos_x.append(24 + (32 * i))
mid_x = 168
fly_left = -64
fly_right = BARS_RIGHT + 64

enemy_path = {
    "group_none": [2137],
    "group_1": [(pos_x[1], top),
                (pos_x[1], middle),
                (fly_left, middle + 64)],
    "group_2": [(pos_x[9], top),
                (pos_x[9], middle),
                (fly_right, bottom_uwu)],
    "group_3": [(mid_x, top),
                (mid_x, middle),
                (mid_x, bottom_uwu)],
    "boss_entry": [(mid_x, top),
                   (mid_x, 68),
                   (mid_x, 72)],
    "boss_loop": [(mid_x, 72),
                  (pos_x[1], 80),
                  (mid_x, 72),
                  (pos_x[9], 80)],
}
