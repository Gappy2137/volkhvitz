from imports import *


def player_render(screen, player):
    screen.blit(PLAYER_SPRITES[int(player.current_frame)], (player.x, player.y))


def hud_render(screen):
    screen.blit(HUD_SPRITES[11], (0, 0))


def bullet_render(screen, _bullet):
    screen.blit(_bullet.SPR[int(_bullet.current_frame)], (_bullet.x, _bullet.y))


def place(screen, enemy):
    screen.blit(enemy.SPR[int(enemy.current_frame)], (enemy.x, enemy.y))


def text_render(screen, text, x, y):
    for char in text:
        index = int(char)
        digit = HUD_SPRITES[index]
        screen.blit(digit, (x, y))
        x += TEXT_WIDTH
