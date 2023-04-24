class Player:
    # Const.
    SPD = 3
    WIDTH = 32
    HEIGHT = 48
    STAT_MOV0 = 0
    STAT_MOV1 = 1
    HITBOX_X = 13
    HITBOX_Y = 25
    HITBOX_SIZE = 8
    ANIM_SPD = 0.15
    # Var.
    can_move = True
    is_moving = False
    x = 200
    y = 200
    hsp = 0
    vsp = 0
