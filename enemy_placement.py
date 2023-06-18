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

    create_enemy(pos_x[0], spawn_y - (32 * 33) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[1], spawn_y - (32 * 34) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[2], spawn_y - (32 * 35) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[3], spawn_y - (32 * 36) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 37) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[5], spawn_y - (32 * 38) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[6], spawn_y - (32 * 38) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 37) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[8], spawn_y - (32 * 36) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[9], spawn_y - (32 * 35) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[10], spawn_y - (32 * 34) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[11], spawn_y - (32 * 33) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))

    create_enemy(pos_x[0], spawn_y - (32 * 30) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[1], spawn_y - (32 * 31) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[2], spawn_y - (32 * 32) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[3], spawn_y - (32 * 33) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 34) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[5], spawn_y - (32 * 35) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[6], spawn_y - (32 * 35) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 34) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[8], spawn_y - (32 * 33) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[9], spawn_y - (32 * 32) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[10], spawn_y - (32 * 31) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[11], spawn_y - (32 * 30) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))

    create_enemy(pos_x[2], spawn_y - (32 * 46), FairyBlue(), enemy_path["group_1"], 1, 0, (0, 2))
    create_enemy(pos_x[9], spawn_y - (32 * 46), FairyBlue(), enemy_path["group_2"], 1, 0, (0, 2))

    group3 = [None] * 6

    group3[0] = create_enemy(pos_x[2], spawn_y - (32 * 62), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group3[1] = create_enemy(pos_x[2], group3[0].y - (32 * 2), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group3[2] = create_enemy(pos_x[2], group3[1].y - (32 * 2), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group3[3] = create_enemy(pos_x[2], group3[2].y - (32 * 2), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group3[4] = create_enemy(pos_x[2], group3[3].y - (32 * 2), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    group3[5] = create_enemy(pos_x[2], group3[4].y - (32 * 2), FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))

    group4 = [None] * 6

    group4[0] = create_enemy(pos_x[9], spawn_y - (32 * 62), FairyRed(), enemy_path["group_2"], 0, 2, (-1, -1))
    group4[1] = create_enemy(pos_x[9], group4[0].y - (32 * 2), FairyRed(), enemy_path["group_2"], 0, 2, (-1, -1))
    group4[2] = create_enemy(pos_x[9], group4[1].y - (32 * 2), FairyRed(), enemy_path["group_2"], 0, 2, (-1, -1))
    group4[3] = create_enemy(pos_x[9], group4[2].y - (32 * 2), FairyRed(), enemy_path["group_2"], 0, 2, (-1, -1))
    group4[4] = create_enemy(pos_x[9], group4[3].y - (32 * 2), FairyRed(), enemy_path["group_2"], 0, 2, (-1, -1))
    group4[5] = create_enemy(pos_x[9], group4[4].y - (32 * 2), FairyRed(), enemy_path["group_2"], 0, 2, (-1, -1))

    create_enemy(pos_x[4], spawn_y - (32 * 67), FairyBlue(), enemy_path["group_down"], 3, 2, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 67), FairyBlue(), enemy_path["group_down"], 3, 2, (-1, -1))

    group5 = [None] * 10

    group5[0] = create_enemy(pos_x[5], spawn_y - (32 * 80), FairyBlue(), enemy_path["group_3"], 0, 2, (-1, -1))
    group5[1] = create_enemy(pos_x[5], group5[0].y - (32 * 1), FairyBlue(), enemy_path["group_3"], 0, 2, (-1, -1))
    group5[2] = create_enemy(pos_x[5], group5[1].y - (32 * 1), FairyBlue(), enemy_path["group_3"], 0, 2, (-1, -1))
    group5[3] = create_enemy(pos_x[5], group5[2].y - (32 * 1), FairyBlue(), enemy_path["group_3"], 0, 2, (-1, -1))
    group5[4] = create_enemy(pos_x[5], group5[3].y - (32 * 1), FairyBlue(), enemy_path["group_3"], 0, 2, (-1, -1))
    group5[5] = create_enemy(pos_x[5], group5[4].y - (32 * 1), FairyBlue(), enemy_path["group_3"], 0, 2, (-1, -1))
    group5[6] = create_enemy(pos_x[5], group5[5].y - (32 * 1), FairyBlue(), enemy_path["group_3"], 0, 2, (-1, -1))
    group5[7] = create_enemy(pos_x[5], group5[6].y - (32 * 1), FairyBlue(), enemy_path["group_3"], 0, 2, (-1, -1))
    group5[8] = create_enemy(pos_x[5], group5[7].y - (32 * 1), FairyBlue(), enemy_path["group_3"], 0, 2, (-1, -1))
    group5[9] = create_enemy(pos_x[5], group5[8].y - (32 * 1), FairyBlue(), enemy_path["group_3"], 0, 2, (-1, -1))

    group6 = [None] * 10

    group6[0] = create_enemy(pos_x[6], spawn_y - (32 * 80), FairyBlue(), enemy_path["group_4"], 0, 2, (-1, -1))
    group6[1] = create_enemy(pos_x[6], group6[0].y - (32 * 1), FairyBlue(), enemy_path["group_4"], 0, 2, (-1, -1))
    group6[2] = create_enemy(pos_x[6], group6[1].y - (32 * 1), FairyBlue(), enemy_path["group_4"], 0, 2, (-1, -1))
    group6[3] = create_enemy(pos_x[6], group6[2].y - (32 * 1), FairyBlue(), enemy_path["group_4"], 0, 2, (-1, -1))
    group6[4] = create_enemy(pos_x[6], group6[3].y - (32 * 1), FairyBlue(), enemy_path["group_4"], 0, 2, (-1, -1))
    group6[5] = create_enemy(pos_x[6], group6[4].y - (32 * 1), FairyBlue(), enemy_path["group_4"], 0, 2, (-1, -1))
    group6[6] = create_enemy(pos_x[6], group6[5].y - (32 * 1), FairyBlue(), enemy_path["group_4"], 0, 2, (-1, -1))
    group6[7] = create_enemy(pos_x[6], group6[6].y - (32 * 1), FairyBlue(), enemy_path["group_4"], 0, 2, (-1, -1))
    group6[8] = create_enemy(pos_x[6], group6[7].y - (32 * 1), FairyBlue(), enemy_path["group_4"], 0, 2, (-1, -1))
    group6[9] = create_enemy(pos_x[6], group6[8].y - (32 * 1), FairyBlue(), enemy_path["group_4"], 0, 2, (-1, -1))

    group7 = [None] * 10

    group7[0] = create_enemy(pos_x[2], spawn_y - (32 * 105), FairyBlue(), enemy_path["group_1"], 0, 0, (-1, -1))
    group7[1] = create_enemy(pos_x[2], group7[0].y - (32 * 1), FairyBlue(), enemy_path["group_1"], 0, 0, (-1, -1))
    group7[2] = create_enemy(pos_x[2], group7[1].y - (32 * 1), FairyBlue(), enemy_path["group_1"], 0, 0, (-1, -1))
    group7[3] = create_enemy(pos_x[2], group7[2].y - (32 * 1), FairyBlue(), enemy_path["group_1"], 0, 0, (-1, -1))
    group7[4] = create_enemy(pos_x[2], group7[3].y - (32 * 1), FairyBlue(), enemy_path["group_1"], 0, 0, (-1, -1))
    group7[5] = create_enemy(pos_x[2], group7[4].y - (32 * 1), FairyBlue(), enemy_path["group_1"], 0, 0, (-1, -1))
    group7[6] = create_enemy(pos_x[2], group7[5].y - (32 * 1), FairyBlue(), enemy_path["group_1"], 0, 0, (-1, -1))
    group7[7] = create_enemy(pos_x[2], group7[6].y - (32 * 1), FairyBlue(), enemy_path["group_1"], 0, 0, (-1, -1))
    group7[8] = create_enemy(pos_x[2], group7[7].y - (32 * 1), FairyBlue(), enemy_path["group_1"], 0, 0, (-1, -1))
    group7[9] = create_enemy(pos_x[2], group7[8].y - (32 * 1), FairyBlue(), enemy_path["group_1"], 0, 0, (-1, -1))

    group8 = [None] * 10

    group8[0] = create_enemy(pos_x[9], spawn_y - (32 * 105), FairyBlue(), enemy_path["group_2"], 0, 3, (-1, -1))
    group8[1] = create_enemy(pos_x[9], group8[0].y - (32 * 1), FairyBlue(), enemy_path["group_2"], 0, 3, (-1, -1))
    group8[2] = create_enemy(pos_x[9], group8[1].y - (32 * 1), FairyBlue(), enemy_path["group_2"], 0, 3, (-1, -1))
    group8[3] = create_enemy(pos_x[9], group8[2].y - (32 * 1), FairyBlue(), enemy_path["group_2"], 0, 3, (-1, -1))
    group8[4] = create_enemy(pos_x[9], group8[3].y - (32 * 1), FairyBlue(), enemy_path["group_2"], 0, 3, (-1, -1))
    group8[5] = create_enemy(pos_x[9], group8[4].y - (32 * 1), FairyBlue(), enemy_path["group_2"], 0, 3, (-1, -1))
    group8[6] = create_enemy(pos_x[9], group8[5].y - (32 * 1), FairyBlue(), enemy_path["group_2"], 0, 3, (-1, -1))
    group8[7] = create_enemy(pos_x[9], group8[6].y - (32 * 1), FairyBlue(), enemy_path["group_2"], 0, 3, (-1, -1))
    group8[8] = create_enemy(pos_x[9], group8[7].y - (32 * 1), FairyBlue(), enemy_path["group_2"], 0, 3, (-1, -1))
    group8[9] = create_enemy(pos_x[9], group8[8].y - (32 * 1), FairyBlue(), enemy_path["group_2"], 0, 3, (-1, -1))

    create_enemy(pos_x[4], spawn_y - (32 * 134) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 135) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 136) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 137) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 138) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 139) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 140) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 141) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 142) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 143) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 144) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 145) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 146) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 147) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 148) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))

    create_enemy(pos_x[7], spawn_y - (32 * 134) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 135) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 136) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 137) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 138) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 139) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 140) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 141) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 142) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 143) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 144) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 145) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 146) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 147) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 148) * 2, Tick(), enemy_path["group_down"], 0, 0, (-1, -1))

    create_enemy(pos_x[2], spawn_y - (32 * 134), FairyBlue(), enemy_path["group_1"], 3, 2, (-1, -1))
    create_enemy(pos_x[2], spawn_y - (32 * 142), FairyBlue(), enemy_path["group_1"], 3, 2, (-1, -1))
    create_enemy(pos_x[9], spawn_y - (32 * 134), FairyBlue(), enemy_path["group_2"], 3, 2, (-1, -1))
    create_enemy(pos_x[9], spawn_y - (32 * 142), FairyBlue(), enemy_path["group_2"], 3, 2, (-1, -1))

    create_enemy(pos_x[2], spawn_y - (32 * 160), Wisp(), enemy_path["group_1"], 0, 1, (-1, -1))
    create_enemy(pos_x[2], spawn_y - (32 * 162), Wisp(), enemy_path["group_1"], 0, 1, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 160), Wisp(), enemy_path["group_down"], 0, 1, (-1, -1))
    create_enemy(pos_x[4], spawn_y - (32 * 162), Wisp(), enemy_path["group_down"], 0, 1, (-1, -1))

    create_enemy(pos_x[9], spawn_y - (32 * 160), Wisp(), enemy_path["group_2"], 0, 1, (-1, -1))
    create_enemy(pos_x[9], spawn_y - (32 * 162), Wisp(), enemy_path["group_2"], 0, 1, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 160), Wisp(), enemy_path["group_down"], 0, 1, (-1, -1))
    create_enemy(pos_x[7], spawn_y - (32 * 162), Wisp(), enemy_path["group_down"], 0, 1, (-1, -1))

    group9 = [None] * 10

    group9[0] = create_enemy(pos_x[2], spawn_y - (32 * 180), Wisp(), enemy_path["group_1"], 0, 0, (-1, -1))
    group9[1] = create_enemy(pos_x[2], group9[0].y - (32 * 1), Wisp(), enemy_path["group_1"], 0, 0, (-1, -1))
    group9[2] = create_enemy(pos_x[2], group9[1].y - (32 * 1), Wisp(), enemy_path["group_1"], 0, 0, (-1, -1))
    group9[3] = create_enemy(pos_x[2], group9[2].y - (32 * 1), Wisp(), enemy_path["group_1"], 0, 0, (-1, -1))
    group9[4] = create_enemy(pos_x[2], group9[3].y - (32 * 1), Wisp(), enemy_path["group_1"], 0, 0, (-1, -1))
    group9[5] = create_enemy(pos_x[2], group9[4].y - (32 * 1), Wisp(), enemy_path["group_1"], 0, 0, (-1, -1))
    group9[6] = create_enemy(pos_x[2], group9[5].y - (32 * 1), Wisp(), enemy_path["group_1"], 0, 0, (-1, -1))
    group9[7] = create_enemy(pos_x[2], group9[6].y - (32 * 1), Wisp(), enemy_path["group_1"], 0, 0, (-1, -1))
    group9[8] = create_enemy(pos_x[2], group9[7].y - (32 * 1), Wisp(), enemy_path["group_1"], 0, 0, (-1, -1))
    group9[9] = create_enemy(pos_x[2], group9[8].y - (32 * 1), Wisp(), enemy_path["group_1"], 0, 0, (-1, -1))

    group10 = [None] * 10

    group10[0] = create_enemy(pos_x[9], spawn_y - (32 * 200), Wisp(), enemy_path["group_2"], 0, 0, (-1, -1))
    group10[1] = create_enemy(pos_x[9], group10[0].y - (32 * 1), Wisp(), enemy_path["group_2"], 0, 0, (-1, -1))
    group10[2] = create_enemy(pos_x[9], group10[1].y - (32 * 1), Wisp(), enemy_path["group_2"], 0, 0, (-1, -1))
    group10[3] = create_enemy(pos_x[9], group10[2].y - (32 * 1), Wisp(), enemy_path["group_2"], 0, 0, (-1, -1))
    group10[4] = create_enemy(pos_x[9], group10[3].y - (32 * 1), Wisp(), enemy_path["group_2"], 0, 0, (-1, -1))
    group10[5] = create_enemy(pos_x[9], group10[4].y - (32 * 1), Wisp(), enemy_path["group_2"], 0, 0, (-1, -1))
    group10[6] = create_enemy(pos_x[9], group10[5].y - (32 * 1), Wisp(), enemy_path["group_2"], 0, 0, (-1, -1))
    group10[7] = create_enemy(pos_x[9], group10[6].y - (32 * 1), Wisp(), enemy_path["group_2"], 0, 0, (-1, -1))
    group10[8] = create_enemy(pos_x[9], group10[7].y - (32 * 1), Wisp(), enemy_path["group_2"], 0, 0, (-1, -1))
    group10[9] = create_enemy(pos_x[9], group10[8].y - (32 * 1), Wisp(), enemy_path["group_2"], 0, 0, (-1, -1))