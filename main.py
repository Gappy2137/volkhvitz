from imports import *

# niewazne jak zle jest to napisane to jest na szybko musisz zrozumiec xdd

if __name__ == '__main__':
    clock = pygame.time.Clock()

    pygame.display.init()
    pygame.mouse.set_visible(False)
    pygame.display.set_caption('Volkhvitz')
    pygame.display.set_icon(pygame.image.load(os.path.join('spritesheet', 'icon.png')))
    screen = pygame.display.set_mode(RESOLUTION, pygame.SCALED)

    player = Player()

    create_enemy(100, 250, FairyRed())
    create_enemy(100, 200, FairyRed())
    create_enemy(100, 100, FairyRed())
    create_enemy(250, 250, FairyBlue())

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
                    in_menu = False
                    in_game = False
                    in_info = True

        if in_menu is True:
            screen.blit(MENU_IMG, (0, 0))
            if opt_check == 'start':
                screen.blit(ARROW_IMG, (490, 317))
            elif opt_check == 'info':
                screen.blit(ARROW_IMG, (490, 350))
            elif opt_check == 'exit':
                screen.blit(ARROW_IMG, (490, 382))

        if in_info is True:
            screen.blit(INFO_IMG, (0, 0))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_info = False
                    in_menu = True

        if in_game is True:

            player.get_keys()

            player.set_speed()

            player.make_move()

            player.set_movement_state()

            player.set_frame()

            screen.fill((255, 100, 255))

            for bullet in bullet_list:
                #pygame.draw.rect(screen, (0, 255, 255), (bullet.x + bullet.hitbox_x, bullet.y + bullet.HITBOX_Y, bullet.width, bullet.HEIGHT))
                for enemy in enemy_list:
                    if collision(bullet.x + bullet.hitbox_x, bullet.y + bullet.HITBOX_Y, bullet.width, bullet.HEIGHT,
                                 enemy.x, enemy.y, enemy.WIDTH, enemy.WIDTH):
                        if not bullet.is_hazard:
                            bullet_list.remove(bullet)
                            #enemy_list.remove(enemy)
                            enemy.health -= bullet.damage
                            create_fx(random.uniform(enemy.x, enemy.x + enemy.WIDTH),
                                      random.uniform(enemy.y + enemy.HEIGHT/2, enemy.y + enemy.HEIGHT),
                                      0, 0, 0, 0, 0, 0.45)
                            if enemy.health <= 0:
                                for i in range(random.randint(6, 12)):
                                    create_fx(random.uniform(enemy.x, enemy.x + enemy.WIDTH),
                                              random.uniform(enemy.y + enemy.HEIGHT / 2, enemy.y + enemy.HEIGHT),
                                              random.uniform(1, 3), random.uniform(2, 4), random.uniform(0, 359), 1, 0, 0.15)

            player.shoot_bullet()

            for bullet in bullet_list:
                bullet.set_frame()
                bullet.make_move()
                bullet.destroy_cond()

            for bullet in bullet_list:
                bullet_render(screen, bullet)

            for enemy in enemy_list:
                enemy.set_frame()
                enemy.check_vitals()

            for enemy in enemy_list:
                enemy_render(screen, enemy)

            for fx in fx_list:
                fx.set_frame()
                fx.make_move()
                fx_render(screen, fx)

            player_render(screen, player)

            hud_render(screen)

            text_render(screen, str(power), POWER_X, POWER_Y)
            #text_render(screen, str(len(fx_list)), POWER_X, POWER_Y + 80)

        pygame.display.flip()

        clock.tick(FPS)
