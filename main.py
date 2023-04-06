import sys
import pygame
import os

import constants as con

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
                    elif opt_check == 'info':
                        in_menu = False
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

        #if in_game is True:

        pygame.display.flip()

        clock.tick(60)
