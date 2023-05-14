from imports import *


def player_render(screen, player):
    screen.blit(PLAYER_SPRITES[int(player.current_frame)], (player.x, player.y))


def hud_render(screen):
    screen.blit(HUD_SPRITES[1], (0, 0))


def place(screen, enemy):
    screen.blit(BLUE_FAIRY_SPRITES[int(enemy.current_frame)], (enemy.x, enemy.y))
