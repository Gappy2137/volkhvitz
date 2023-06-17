from imports import *


def bg_render(screen, bg):
    screen.blit(bg.SPR[int(bg.frame)], (16, bg.y))


def fx_render(screen, fx):
    screen.blit(fx.SPR[int(fx.current_frame)], (fx.x, fx.y))


def enemy_render(screen, enemy):
    screen.blit(enemy.SPR[int(enemy.current_frame)], (enemy.x, enemy.y))

def powerup_render(screen, powerup):
    screen.blit(FX_SPRITES[9], (powerup.x, powerup.y))


def bullet_render(screen, bullet):
    screen.blit(bullet.SPR[int(bullet.current_frame)], (bullet.x, bullet.y))



def player_render(screen, player):
    if player.visible:
        screen.blit(PLAYER_SPRITES[int(player.current_frame)], (player.x, player.y))


def player_hitbox_render(screen, player):
    screen.blit(PLAYER_SPRITES[4], (player.x, player.y))


def hud_render(screen):
    screen.blit(HUD_SPRITES[11], (0, 0))


def text_render(screen, text, x, y):
    for char in text:
        index = int(char)
        digit = HUD_SPRITES[index]
        screen.blit(digit, (x, y))
        x += TEXT_WIDTH