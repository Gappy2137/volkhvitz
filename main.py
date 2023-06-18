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

    #en = [None] * 11

    #en[0] = create_enemy(pos_x[1], spawn_y, FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    #en[1] = create_enemy(pos_x[1], en[0].y - 32, FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    #en[2] = create_enemy(pos_x[1], en[1].y - 32, FairyRed(), enemy_path["group_1"], 0, 0, (-1, -1))
    #create_enemy(spawn_x, spawn_y - 64, FairyRed(), enemy_path["group_1"], 2)
    #create_enemy(spawn_x, spawn_y, FairyRed(), enemy_path["group_2"], 0)
    #create_enemy(spawn_x, spawn_y - 32, FairyRed(), enemy_path["group_2"], 1)
    #create_enemy(spawn_x, spawn_y - 64, FairyRed(), enemy_path["group_2"], 2)

    #create_enemy(spawn_x, spawn_y - 256, FairyBlue(), enemy_path["group_3"], 0)
    #create_enemy(200, 200, FairyBlue(), enemy_path["group_1"], 2, 0, (0, 1))
    boss = create_enemy(spawn_x, spawn_y - (32 * 220) * 1.6, Boss(), enemy_path["boss_entry"], 0, 0, (-1, -1))
    #create_enemy(64, 200, FairyRed(), enemy_path["group_none"], 0, 0, (-1, -1))


    enemy_place()


    screen.fill((0, 0, 0))

    bg = Background()
    bg2 = Background()
    bg2.y = -bg2.HEIGHT * 2 + 480

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

            keyss = pygame.key.get_pressed()
            if keyss[pygame.K_a]:
                psl[0] -= 1
            if keyss[pygame.K_d]:
                psl[0] += 1

            player.get_keys()

            player.set_speed()

            player.make_move()

            player.set_movement_state()

            player.set_frame()

            player.invis_logic()

            #screen.fill((255, 100, 255))
            bg.set_frame(0)
            bg.make_scroll(True)
            bg2.set_frame(0)
            bg2.make_scroll(False)

            if bg.y >= RESOLUTION[1]:
                bg.y = bg2.y - bg2.HEIGHT
            if bg2.y >= RESOLUTION[1]:
                bg2.y = bg.y - bg.HEIGHT

            bg_render(screen, bg)
            bg_render(screen, bg2)


            for bullet in bullet_list:
                #pygame.draw.rect(screen, (0, 255, 255), (bullet.x + bullet.hitbox_x, bullet.y + bullet.hitbox_x, bullet.width, bullet.height))
                if bullet.is_hazard:
                    if collision(bullet.x + bullet.hitbox_x, bullet.y + bullet.hitbox_y, bullet.width, bullet.height,
                                 player.x + player.HITBOX_X, player.y + player.HITBOX_Y, player.HITBOX_SIZE, player.HITBOX_SIZE):
                        #bullet_list.remove(bullet)
                        bullet_remove_list.append(bullet)
                        player.hit()
                for enemy in enemy_list:
                    if collision(bullet.x + bullet.hitbox_x, bullet.y + bullet.hitbox_y, bullet.width, bullet.height,
                                 enemy.x, enemy.y, enemy.WIDTH, enemy.WIDTH):
                        if not bullet.is_hazard:
                            # bullet_list.remove(bullet)
                            bullet_remove_list.append(bullet)
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

            for bullet in bullet_remove_list:
                if bullet in bullet_list:
                    bullet_list.remove(bullet)

            if enemy_list.__len__() > 0:
                min_distance = float('inf')
                xx = 0
                yy = 0
                for enemy in enemy_list:
                    dist = calc_distance(player.x, player.y, enemy.x, enemy.y)
                    if dist < min_distance:
                        min_distance = dist
                        xx = enemy.x
                        yy = enemy.y

                player.shoot_bullet(xx, yy)
            else:
                player.shoot_bullet(player.x + player.WIDTH / 2, 0)

            for enemy in enemy_list:
                enemy.set_frame()
                enemy.check_vitals()
                enemy.make_move()
                if collision(enemy.x + enemy.HITBOX_X, enemy.y + enemy.HITBOX_Y, enemy.HITBOX_SIZE, enemy.HITBOX_SIZE,
                             player.x + player.HITBOX_X, player.y + player.HITBOX_Y, player.HITBOX_SIZE, player.HITBOX_SIZE):
                    player.hit()
                if enemy.y > BARS_BOTTOM + 64:
                    enemy.destroy(False)
                enemy.shoot_bullet(player.x + player.WIDTH/2, player.y + player.HEIGHT/2, 1)

            for enemy in enemy_list:
                enemy_render(screen, enemy)

            for fx in fx_list:
                fx.set_frame()
                fx.make_move()
                fx_render(screen, fx)

            for powerup in powerup_list:
                powerup.make_move()
                powerup.destroy_cond()
                if collision(player.x, player.y, player.WIDTH, player.HEIGHT,
                             powerup.x, powerup.y, powerup.SIZE, powerup.SIZE):
                    powerup.collect()

            for powerup in powerup_list:
                powerup_render(screen, powerup)

            player_render(screen, player)

            if player.show_hitbox:
                player_hitbox_render(screen, player)

            for bullet in bullet_list:
                bullet.set_frame()
                bullet.make_move()
                bullet.destroy_cond()

            for bullet in bullet_list:
                bullet_render(screen, bullet)

            hud_render(screen)

            if psl[0] > 128:
                psl[0] = 128

            if psl[1] > 9999999999:
                psl[1] = 9999999999

            if psl[2] <= 0:
                pygame.quit()
                sys.exit()

            text_render(screen, str(psl[0]), POWER_X, POWER_Y)
            text_render(screen, f"{psl[1]:04}", SCORE_X, SCORE_Y)

            for i in range(psl[2]):
                screen.blit(HUD_SPRITES[10], (LIVES_X + (i % 5) * 32, LIVES_Y + (i // 5) * 32))

            if boss.move_pattern > 0:
                health_percentage = boss.health / boss.health_max
                health_bar_width = int(health_percentage * 368 - 8)

                pygame.draw.rect(screen, (255, 0, 0), (16 + 16, 2, health_bar_width - 8, 14))

        pygame.display.flip()

        clock.tick(FPS)
