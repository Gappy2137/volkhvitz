import sys
import pygame
import os
from core.variables import *
from core.classes import *

if __name__ == '__main__':
    pygame.display.init()
    pygame.display.set_caption('Volkhvitz')
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()

    pygame.display.set_icon(pygame.image.load(os.path.join('spritesheet', 'icon.png')))
    screen = pygame.display.set_mode(RESOLUTION, pygame.SCALED)

    screen.fill((0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if in_menu is True:
                    if event.key == pygame.K_UP:
                        opt_num = opt_num - 1
                        if opt_num < 0:
                            opt_num = 2
                        opt_check = OPTIONS[opt_num]
                    if event.key == pygame.K_DOWN:
                        opt_num = opt_num + 1
                        if opt_num > 2:
                            opt_num = 0
                        opt_check = OPTIONS[opt_num]
                    if event.key == pygame.K_RETURN:
                        if opt_check == 'start':
                            in_menu = False
                            in_game = True
                            in_info = False
                        elif opt_check == 'info':
                            in_menu = False
                            in_game = False
                            in_info = True
                            screen.fill((0, 0, 0))
                            screen.blit(ARROW_IMG, (490, 350))
                        elif opt_check == 'exit':
                            pygame.quit()
                            sys.exit()

        if in_menu is True:
            screen.blit(MENU_IMG, (0, 0))
            if opt_check == 'start':
                screen.blit(ARROW_IMG, (490, 317))
            elif opt_check == 'info':
                screen.blit(ARROW_IMG, (490, 350))
            elif opt_check == 'exit':
                screen.blit(ARROW_IMG, (490, 382))

        if in_game is True:

            keys = pygame.key.get_pressed()

            if Player.can_move:
                if keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
                    Player.vsp = Player.SPD
                elif keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                    Player.vsp = -Player.SPD
                else:
                    Player.vsp = 0

                if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    Player.hsp = -Player.SPD
                elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                    Player.hsp = Player.SPD
                else:
                    Player.hsp = 0

            Player.x += Player.hsp
            Player.y += Player.vsp

            if Player.hsp and Player.vsp != 0:
                Player.is_moving = True
            else:
                Player.is_moving = False

            if Player.hsp < 0:
                Player.STAT_MOV0 = 2
            elif Player.hsp > 0:
                Player.STAT_MOV0 = 3
            elif Player.hsp == 0:
                Player.STAT_MOV0 += Player.ANIM_SPD
                if Player.STAT_MOV0 >= Player.STAT_MOV1 + 0.9:
                    Player.STAT_MOV0 = 0

            screen.fill((255, 255, 255))

            screen.blit(PLAYER_SPRITES[int(Player.STAT_MOV0)], (Player.x, Player.y))

        pygame.display.flip()

        clock.tick(FPS)
