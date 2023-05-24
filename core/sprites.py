"""Sprites."""
from imports import *

BULLETS_SPRITES = [pygame.image.load(os.path.join(DIR + r'\spritesheet\bullets', 'enemy_bullet_big.png')),
                   pygame.image.load(os.path.join(DIR + r'\spritesheet\bullets', 'enemy_bullet_small.png')),
                   pygame.image.load(os.path.join(DIR + r'\spritesheet\bullets', 'player_bullet_hit_frame_0.png')),
                   pygame.image.load(os.path.join(DIR + r'\spritesheet\bullets', 'player_bullet_hit_frame_1.png')),
                   pygame.image.load(os.path.join(DIR + r'\spritesheet\bullets', 'player_bullet_hit_frame_2.png')),
                   pygame.image.load(os.path.join(DIR + r'\spritesheet\bullets', 'player_bullet_hit_frame_3.png')),
                   pygame.image.load(os.path.join(DIR + r'\spritesheet\bullets', 'player_bullet_hit_frame_4.png')),
                   pygame.image.load(os.path.join(DIR + r'\spritesheet\bullets', 'player_bullet_power_0.png'))]

BLUE_FAIRY_SPRITES = [pygame.image.load(os.path.join(DIR + r'\spritesheet\fairy_blue', 'fairy_blue_frame_0.png')),
                      pygame.image.load(os.path.join(DIR + r'\spritesheet\fairy_blue', 'fairy_blue_frame_1.png')),
                      pygame.image.load(os.path.join(DIR + r'\spritesheet\fairy_blue', 'fairy_blue_frame_2.png')),
                      pygame.image.load(os.path.join(DIR + r'\spritesheet\fairy_blue', 'fairy_blue_frame_3.png'))]

RED_FAIRY_SPRITES = [pygame.image.load(os.path.join(DIR + r'\spritesheet\fairy_red', 'fairy_red_frame_0.png')),
                     pygame.image.load(os.path.join(DIR + r'\spritesheet\fairy_red', 'fairy_red_frame_1.png')),
                     pygame.image.load(os.path.join(DIR + r'\spritesheet\fairy_red', 'fairy_red_frame_2.png')),
                     pygame.image.load(os.path.join(DIR + r'\spritesheet\fairy_red', 'fairy_red_frame_3.png'))]

HUD_SPRITES = [pygame.image.load(os.path.join(DIR + r'\spritesheet\hud', 'hud_life.png')),
               pygame.image.load(os.path.join(DIR + r'\spritesheet\hud', 'main_hud.png')),
               pygame.image.load(os.path.join(DIR + r'\spritesheet\hud', 'number_0.png')),
               pygame.image.load(os.path.join(DIR + r'\spritesheet\hud', 'number_1.png')),
               pygame.image.load(os.path.join(DIR + r'\spritesheet\hud', 'number_2.png')),
               pygame.image.load(os.path.join(DIR + r'\spritesheet\hud', 'number_3.png')),
               pygame.image.load(os.path.join(DIR + r'\spritesheet\hud', 'number_4.png')),
               pygame.image.load(os.path.join(DIR + r'\spritesheet\hud', 'number_5.png')),
               pygame.image.load(os.path.join(DIR + r'\spritesheet\hud', 'number_6.png')),
               pygame.image.load(os.path.join(DIR + r'\spritesheet\hud', 'number_7.png')),
               pygame.image.load(os.path.join(DIR + r'\spritesheet\hud', 'number_8.png')),
               pygame.image.load(os.path.join(DIR + r'\spritesheet\hud', 'number_9.png'))]

PLAYER_SPRITES = [pygame.image.load(os.path.join(DIR + r'\spritesheet\player', 'player_frame_0.png')),
                  pygame.image.load(os.path.join(DIR + r'\spritesheet\player', 'player_frame_1.png')),
                  pygame.image.load(os.path.join(DIR + r'\spritesheet\player', 'player_frame_left.png')),
                  pygame.image.load(os.path.join(DIR + r'\spritesheet\player', 'player_frame_right.png'))]
