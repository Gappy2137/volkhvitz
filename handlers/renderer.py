from imports import *


def player_render(screen, player):
    screen.blit(PLAYER_SPRITES[int(player.current_frame)], (player.x, player.y))
