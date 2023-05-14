from imports import *

if __name__ == '__main__':
    pygame.display.init()
    pygame.display.set_caption('Volkhvitz')
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()

    pygame.display.set_icon(pygame.image.load(os.path.join('spritesheet', 'icon.png')))
    screen = pygame.display.set_mode(RESOLUTION, pygame.SCALED)

    player = Player()

    screen.fill((0, 0, 0))

    while True:
        for event in pygame.event.get():
            # Quit event.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Menu option choice.
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
                        elif opt_check == 'exit':
                            pygame.quit()
                            sys.exit()

                if in_info is True:
                    in_menu = True
                    in_game = False
                    in_info = False

        if in_menu is True:
            screen.blit(MENU_IMG, (0, 0))
            if opt_check == 'start':
                screen.blit(ARROW_IMG, (490, 317))
            elif opt_check == 'info':
                screen.blit(ARROW_IMG, (490, 350))
            elif opt_check == 'exit':
                screen.blit(ARROW_IMG, (490, 382))

        if in_info is True:
            # screen.blit(INFO_IMG, (0, 0))
            pass

        if in_game is True:
            player.get_keys()

            player.set_speed()

            player.make_move()

            player.set_movement_state()

            player.set_frame()

            screen.fill((255, 255, 255))

            player_render(screen, player)

        pygame.display.flip()

        clock.tick(FPS)
