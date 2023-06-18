from imports import *

enemy_list = []

spawn_x = 192
spawn_y = -128
top = -32
switch = 224
bottom_uwu = 640
pos_x = [16]
for i in range(1, 12):
    pos_x.append(16 + (32 * i))
mid_x = 168 + 16
fly_left = -64
fly_right = BARS_RIGHT + 64

enemy_path = {
    "group_none": [2137],
    "group_1": [(pos_x[2], top),
                (pos_x[2], switch),
                (fly_left, bottom_uwu)],
    "group_2": [(pos_x[9], top),
                (pos_x[9], switch),
                (fly_right, switch + 80)],
    "group_3": [(pos_x[5], top),
                (pos_x[5], switch - 32),
                (fly_left, switch + 16)],
    "group_4": [(pos_x[6], top),
                (pos_x[6], switch - 32),
                (fly_right, switch + 16)],
    "group_5": [(mid_x, top),
                (mid_x, switch),
                (mid_x, bottom_uwu)],
    "group_down": [2138],
    "boss_entry": [(mid_x, top),
                   (mid_x, 60),
                   (mid_x, 66),
                   (mid_x, 70),
                   (mid_x, 72)],
    "boss_loop": [(mid_x, 72),
                  (pos_x[1], 80),
                  (mid_x, 72),
                  (pos_x[9], 80)],
}
