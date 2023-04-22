import sys
import pygame
import os

import constants as con
import playerVars as player

options = ['start', 'info', 'exit']
opt_num = 0
opt_check = options[opt_num]

if __name__ == '__main__':
    pygame.display.init()
    pygame.display.set_caption('Volkhvitz')

    clock = pygame.time.Clock()

    pygame.display.set_icon(pygame.image.load(os.path.join('spritesheet', 'icon.png')))

    menu_img = pygame.image.load(os.path.join('spritesheet', 'menu.png'))
    arrow_img = pygame.image.load(os.path.join('spritesheet', 'arrow.png'))

    sprite_player = [pygame.image.load(os.path.join('spritesheet', 'player_frame_0.png')),
                     pygame.image.load(os.path.join('spritesheet', 'player_frame_1.png')),
                     pygame.image.load(os.path.join('spritesheet', 'player_frame_left.png')),
                     pygame.image.load(os.path.join('spritesheet', 'player_frame_right.png'))]

    screen = pygame.display.set_mode([con.SCR_WIDTH, con.SCR_HEIGHT], pygame.SCALED)

    screen.fill((0, 0, 0))

    in_menu = True
    in_game = False
    in_info = False

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
                        opt_check = options[opt_num]
                    if event.key == pygame.K_DOWN:
                        opt_num = opt_num + 1
                        if opt_num > 2:
                            opt_num = 0
                        opt_check = options[opt_num]
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
                            screen.blit(arrow_img, (490, 350))
                        elif opt_check == 'exit':
                            pygame.quit()
                            sys.exit()

        if in_menu is True:
            screen.blit(menu_img, (0, 0))
            if opt_check == 'start':
                screen.blit(arrow_img, (490, 317))
            elif opt_check == 'info':
                screen.blit(arrow_img, (490, 350))
            elif opt_check == 'exit':
                screen.blit(arrow_img, (490, 382))

        if in_game is True:

            keys = pygame.key.get_pressed()

            if player.canMove:
                if keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
                    player.vsp = player.spd
                elif keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                    player.vsp = -player.spd
                else:
                    player.vsp = 0

                if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    player.hsp = -player.spd
                elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                    player.hsp = player.spd
                else:
                    player.hsp = 0

            player.x += player.hsp
            player.y += player.vsp

            if player.hsp and player.vsp != 0:
                player.moving = True
            else:
                player.moving = False

            if player.hsp < 0:
                player.animFrame = 2
            elif player.hsp > 0:
                player.animFrame = 3
            elif player.hsp == 0:
                player.animFrame += player.animSpeed
                if player.animFrame >= player.animFrames + 0.9:
                    player.animFrame = 0

            #background
            screen.fill((255, 255, 255))

            screen.blit(sprite_player[int(player.animFrame)], (player.x, player.y))

        pygame.display.flip()

        clock.tick(60)
