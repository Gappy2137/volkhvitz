from imports import *


def enemy_place():
    group1 = [None] * 10

    group1[0] = create_enemy(pos_x[3], spawn_y - (32 * 1), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group1[1] = create_enemy(pos_x[3], group1[0].y - (32 * 1), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group1[2] = create_enemy(pos_x[3], group1[1].y - (32 * 1), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group1[3] = create_enemy(pos_x[3], group1[2].y - (32 * 1), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group1[4] = create_enemy(pos_x[3], group1[3].y - (32 * 1), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group1[5] = create_enemy(pos_x[3], group1[4].y - (32 * 1), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group1[6] = create_enemy(pos_x[3], group1[5].y - (32 * 1), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group1[7] = create_enemy(pos_x[3], group1[6].y - (32 * 1), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group1[8] = create_enemy(pos_x[3], group1[7].y - (32 * 1), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group1[9] = create_enemy(pos_x[3], group1[8].y - (32 * 1), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))

    group2 = [None] * 10

    group2[0] = create_enemy(pos_x[9], spawn_y - (32 * 16), FairyRed(), enemy_path["group_2"], 0, 0, (-1, -1))
    group2[1] = create_enemy(pos_x[9], group2[0].y - (32 * 1), FairyRed(), enemy_path["group_2"], 0, 0, (-1, -1))
    group2[2] = create_enemy(pos_x[9], group2[1].y - (32 * 1), FairyRed(), enemy_path["group_2"], 0, 0, (-1, -1))
    group2[3] = create_enemy(pos_x[9], group2[2].y - (32 * 1), FairyRed(), enemy_path["group_2"], 0, 0, (-1, -1))
    group2[4] = create_enemy(pos_x[9], group2[3].y - (32 * 1), FairyRed(), enemy_path["group_2"], 0, 0, (-1, -1))
    group2[5] = create_enemy(pos_x[9], group2[4].y - (32 * 1), FairyRed(), enemy_path["group_2"], 0, 0, (-1, -1))
    group2[6] = create_enemy(pos_x[9], group2[5].y - (32 * 1), FairyRed(), enemy_path["group_2"], 0, 0, (-1, -1))
    group2[7] = create_enemy(pos_x[9], group2[6].y - (32 * 1), FairyRed(), enemy_path["group_2"], 0, 0, (-1, -1))
    group2[8] = create_enemy(pos_x[9], group2[7].y - (32 * 1), FairyRed(), enemy_path["group_2"], 0, 0, (-1, -1))
    group2[9] = create_enemy(pos_x[9], group2[8].y - (32 * 1), FairyRed(), enemy_path["group_2"], 0, 0, (-1, -1))

    create_enemy(pos_x[0], spawn_y - (32 * 33), FairyRed(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[1], spawn_y - (32 * 34), FairyRed(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[2], spawn_y - (32 * 35), FairyRed(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[3], spawn_y - (32 * 36), FairyRed(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 37), FairyRed(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[5], spawn_y - (32 * 38), FairyRed(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[6], spawn_y - (32 * 38), FairyRed(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 37), FairyRed(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[8], spawn_y - (32 * 36), FairyRed(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[9], spawn_y - (32 * 35), FairyRed(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[10], spawn_y - (32 * 34), FairyRed(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[11], spawn_y - (32 * 33), FairyRed(), enemy_path["group_down"], 0, 0, (-1, -1))

    create_enemy(pos_x[2], spawn_y - (32 * 43), FairyBlue(), enemy_path["group_1"], 1, 0, (0, 2))
    create_enemy(pos_x[9], spawn_y - (32 * 43), FairyBlue(), enemy_path["group_2"], 1, 0, (0, 2))

