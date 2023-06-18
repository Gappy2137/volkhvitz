"""Classes."""
import random

from imports import *


class Player:
    def __init__(self):
        # Const.
        self.SPD = 3
        self.WIDTH = 32
        self.HEIGHT = 48
        self.HITBOX_X = 13
        self.HITBOX_Y = 25
        self.HITBOX_SIZE = 6
        self.ANIM_SPD = 0.15
        self.DIAG_MULTIPLIER = 0.75
        self.FOCUS_MULTIPLIER = 0.5
        self.BULLET_SHOOTING_FREQ = 3
        # Var.
        self.keys = []
        self.current_frame = 0
        self.curr_anim_no_of_frs = 1
        self.can_move = True
        self.is_moving = False
        self.can_shoot = True
        self.x = 180
        self.y = 370
        self.hsp = 0
        self.vsp = 0
        self.bullet_clock = 0
        self.bullet_type = 0
        self.show_hitbox = False
        self.invis = False
        self.invis_duration = 120
        self.invis_clock = self.invis_duration
        self.visible = True

    def get_keys(self):
        self.keys = pygame.key.get_pressed()

    def set_movement_state(self):
        if self.hsp and self.vsp != 0:
            self.is_moving = True
        else:
            self.is_moving = False

    def set_speed(self):
        if self.can_move:
            if self.keys[pygame.K_DOWN] and not self.keys[pygame.K_UP]:
                if not (self.y + self.HEIGHT >= BARS_BOTTOM):
                    self.vsp = self.SPD
                else:
                    self.vsp = 0
            elif self.keys[pygame.K_UP] and not self.keys[pygame.K_DOWN]:
                if not (self.y < BARS_TOP):
                    self.vsp = -self.SPD
                else:
                    self.vsp = 0
            else:
                self.vsp = 0

            if self.keys[pygame.K_LEFT] and not self.keys[pygame.K_RIGHT]:
                if not (self.x< BARS_LEFT):
                    self.hsp = -self.SPD
                else:
                    self.hsp = 0
            elif self.keys[pygame.K_RIGHT] and not self.keys[pygame.K_LEFT]:
                if not (self.x + self.WIDTH >= BARS_RIGHT):
                    self.hsp = self.SPD
                else:
                    self.hsp = 0
            else:
                self.hsp = 0

            if abs(self.hsp) == abs(self.SPD) and abs(self.vsp) == abs(self.SPD):
                self.hsp *= self.DIAG_MULTIPLIER
                self.vsp *= self.DIAG_MULTIPLIER

            if self.keys[pygame.K_LSHIFT]:
                self.show_hitbox = True
                self.hsp *= self.FOCUS_MULTIPLIER
                self.vsp *= self.FOCUS_MULTIPLIER
            else:
                self.show_hitbox = False

    def make_move(self):
        self.x += self.hsp
        self.y += self.vsp

    def set_frame(self):
        if self.hsp < 0:
            self.current_frame = 2
        elif self.hsp > 0:
            self.current_frame = 3
        elif self.hsp == 0:
            self.current_frame += self.ANIM_SPD
            if self.current_frame >= self.curr_anim_no_of_frs + 0.9:
                self.current_frame = 0

    def shoot_bullet(self, to_x, to_y):

        if psl[0] in range(0, 31):
            self.bullet_type = 0
        elif psl[0] in range(32, 79):
            self.bullet_type = 2
        elif psl[0] in range(80, 127):
            self.bullet_type = 3
        elif psl[0] in range(128, 164):
            self.bullet_type = 4

        if self.keys[pygame.K_z]:
            if self.can_shoot is True:
                create_bullet(self.x + self.WIDTH/2, self.y, False, False, 0, 0, self.bullet_type, 0, False)
                if self.bullet_type == 3:
                    create_bullet(self.x + self.WIDTH / 2, self.y, False, True, to_x, to_y, self.bullet_type, 0, True)
                if self.bullet_type == 4:
                    create_bullet(self.x - 2, self.y + 12, False, True, to_x, to_y, self.bullet_type, 0, True)
                    create_bullet(self.x + self.WIDTH, self.y + 12, False, True, to_x, to_y, self.bullet_type, 0, True)
                self.can_shoot = False
        else:
            self.can_shoot = True

        if self.can_shoot is False:
            self.bullet_clock += 1
            if self.bullet_clock > self.BULLET_SHOOTING_FREQ:
                self.bullet_clock = 0

        if self.bullet_clock == 0:
            self.can_shoot = True

    def hit(self):
        if not self.invis:
            psl[0] -= math.floor(psl[0] / 3)
            psl[2] -= 1
            self.invis = True

    def invis_logic(self):
        if self.invis:
            self.invis_clock -= 1

            if self.invis_clock % 2 == 0:
                self.visible = True
            else:
                self.visible = False

            if self.invis_clock == 0:
                self.invis_clock = self.invis_duration
                self.invis = False


class Enemy:
    def __init__(self):
        # Const.
        self.SPR = []
        self.SPD = 1
        self.WIDTH = 32
        self.HEIGHT = 32
        self.HITBOX_X = 13
        self.HITBOX_Y = 25
        self.HITBOX_SIZE = 8
        self.BULLET_HITBOX_X = 0
        self.BULLET_HITBOX_Y = 0
        self.ANIM_SPD = 0.15
        self.SHOOTING_CAPABLE = True
        # Var.
        self.start_shooting_delay = random.randint(0, 255)
        self.bullet_init_freq = 20
        self.bullet_shooting_freq = self.bullet_init_freq
        self.current_frame = 0
        self.curr_anim_no_of_frs = 3
        self.can_move = True
        self.is_moving = False
        self.move_pattern = 0
        self.change_pattern = (-1, -1)

        self.bullet_freq = 0
        # 0 - shoot with bullet_shoot_freq interval
        # 1 - shoot 2x faster
        # 2 - shoot 2x slower
        # 3 - shoot in random intervals (20, 80)
        # 4 - shoot 3x faster
        # 5 - shoot 4x faster

        self.bullet_pattern = 0
        # 0 - shoot 1 bullet
        # 1 - shoot 3 bullets with 5-degree angle difference
        # 2 - shoot in a circle (8 bullets)
        # 3 - shoot in a circle (16 bullets)

        self.bullet_type = 1
        self.x = 180
        self.y = 170
        self.hsp = 0
        self.vsp = 0
        self.can_shoot = True
        self.bullet_clock = 0
        self.health = 2
        self.score_on_kill = 100
        self.waypoints = 0
        self.waypoint_index = 0
        self.following = 0

    def set_frame(self):
        self.current_frame += self.ANIM_SPD
        if self.current_frame >= self.curr_anim_no_of_frs + 0.9:
            self.current_frame = 0

    def make_move(self):

        if not self.waypoints[self.change_pattern[0]] == -1:
            if self.waypoint_index == self.change_pattern[1]:
                self.bullet_set_pattern(self.change_pattern[0])

        if self.waypoints[0] == 2137:
            return
        if not isinstance(self.following, Enemy):
            target_x, target_y = self.waypoints[self.waypoint_index]
        else:
            target_x, target_y = self.following.x, self.following.y
        dx = target_x - self.x
        dy = target_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < self.SPD:
            self.waypoint_index += 1
            if self.waypoint_index >= len(self.waypoints):
                self.destroy(False)
            else:
                if not isinstance(self.following, Enemy):
                    target_x, target_y = self.waypoints[self.waypoint_index]
                else:
                    target_x, target_y = self.following.x, self.following.y
                dx = target_x - self.x
                dy = target_y - self.y

        angle = math.atan2(dy, dx)
        self.x += self.SPD * math.cos(angle)
        self.y += self.SPD * math.sin(angle)

    def bullet_set_freq(self):
        if self.bullet_freq == 0:
            self.bullet_shooting_freq = self.bullet_init_freq
        elif self.bullet_freq == 1:
            self.bullet_shooting_freq = self.bullet_init_freq // 2
        elif self.bullet_freq == 2:
            self.bullet_shooting_freq = self.bullet_init_freq * 2
        elif self.bullet_freq == 3:
            self.bullet_shooting_freq = random.randint(20, 80)
        elif self.bullet_freq == 4:
            self.bullet_shooting_freq = self.bullet_init_freq // 3
        elif self.bullet_freq == 5:
            self.bullet_shooting_freq = self.bullet_init_freq // 4

    def bullet_set_pattern(self, bullet_pattern):
        self.bullet_pattern = bullet_pattern

    def shoot_bullet(self, to_x, to_y, bullet_type):

        if not self.SHOOTING_CAPABLE:
            return

        self.start_shooting_delay -= 1
        if self.start_shooting_delay <= 0:
            self.start_shooting_delay = 0

            if self.can_shoot is True:

                if self.bullet_pattern == 0:
                    create_bullet(self.x + self.WIDTH/2, self.y + self.HEIGHT/2, True, True, to_x, to_y, bullet_type, 0, False)
                elif self.bullet_pattern == 1:
                    create_bullet(self.x + self.WIDTH / 2, self.y + self.HEIGHT / 2, True, True, to_x, to_y, bullet_type, 0, False)
                    create_bullet(self.x + self.WIDTH / 2, self.y + self.HEIGHT / 2, True, True, to_x, to_y, bullet_type, 10, False)
                    create_bullet(self.x + self.WIDTH / 2, self.y + self.HEIGHT / 2, True, True, to_x, to_y, bullet_type, -10, False)
                elif self.bullet_pattern == 2:
                    for i in range(8):
                        create_bullet(self.x + self.WIDTH / 2, self.y + self.HEIGHT / 2, True, True, to_x, to_y, bullet_type, (i * 45), False)
                elif self.bullet_pattern == 3:
                    for i in range(16):
                        create_bullet(self.x + self.WIDTH / 2, self.y + self.HEIGHT / 2, True, True, to_x, to_y, bullet_type, (i * 22.5), False)

                self.can_shoot = False

            if self.can_shoot is False:
                self.bullet_clock += 1
                if self.bullet_clock > self.bullet_shooting_freq:
                    self.bullet_clock = 0
                    self.can_shoot = True

    def check_vitals(self):
        if self.health <= 0:
            self.destroy(True)

    def destroy(self, give_points):
        if give_points:
            psl[1] += self.score_on_kill
            create_powerup(self.x + self.WIDTH / 2, self.y + self.HEIGHT / 2)
        enemy_list.remove(self)
        del self


class FairyRed(Enemy):
    def __init__(self):
        super().__init__()
        self.SPR = RED_FAIRY_SPRITES
        self.WIDTH = 32
        self.HEIGHT = 32
        self.HITBOX_X = 10
        self.HITBOX_Y = 11
        self.HITBOX_SIZE = 12
        self.bullet_shooting_freq = random.randint(30, 50)
        self.bullet_type = 0


class FairyBlue(FairyRed):
    def __init__(self):
        super().__init__()
        self.SPR = BLUE_FAIRY_SPRITES
        self.health = 8
        self.bullet_type = 0
        self.bullet_shooting_freq = 20


class Wisp(Enemy):
    def __init__(self):
        super().__init__()
        self.SPR = WISP_SPRITES
        self.WIDTH = 32
        self.HEIGHT = 32
        self.HITBOX_X = 11
        self.HITBOX_Y = 17
        self.HITBOX_SIZE = 9
        self.health = 4
        self.SPD = 2
        self.ANIM_SPD = 0.2
        self.bullet_shooting_freq = random.randint(60, 120)
        self.bullet_type = 0


class Tick(Enemy):
    def __init__(self):
        super().__init__()
        self.SPR = TICK_SPRITES
        self.WIDTH = 32
        self.HEIGHT = 32
        self.HITBOX_X = 12
        self.HITBOX_Y = 13
        self.HITBOX_SIZE = 7
        self.SHOOTING_CAPABLE = False
        self.SPD = 3
        self.ANIM_SPD = 1
        self.health = 1


class Boss(Enemy):

    def __init__(self):
        super().__init__()
        self.SPR = BOSS_SPRITES
        self.WIDTH = 48
        self.HEIGHT = 64
        self.HITBOX_X = 16
        self.HITBOX_Y = 22
        self.HITBOX_SIZE = 11
        self.SPD = 2
        self.ANIM_SPD = 0.12
        self.health_max = 500
        self.health = self.health_max
        # 0 - moving, 1 - attack
        self.state = 0
        # 0 - move to place, 1 - fly left and right, 2 - fly in middle
        self.move_pattern = 0
        self.ready = False
        self.change_timer_1_init = 60 * 10
        self.change_timer_1 = self.change_timer_1_init

    def set_init_frame(self):
        if self.state == 0:
            self.current_frame = 0
            self.curr_anim_no_of_frs = 3
        else:
            self.current_frame = 4
            self.curr_anim_no_of_frs = 7

    def set_frame(self):
        self.current_frame += self.ANIM_SPD
        if self.current_frame >= self.curr_anim_no_of_frs + 0.9:
            self.current_frame = 0

    def make_move(self):
        if self.waypoints[0] == 2137:
            return

        target_x, target_y = self.waypoints[self.waypoint_index]
        dx = target_x - self.x
        dy = target_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < self.SPD:
            self.waypoint_index += 1

        if self.move_pattern == 0:
            if self.waypoint_index > 2:
                self.waypoint_index = 0
                self.waypoints = enemy_path["boss_loop"]
                self.move_pattern = 1

        if self.move_pattern == 1:
            self.change_timer_1 -= 1
            if self.waypoint_index > 3:
                self.waypoint_index = 0
            target_x, target_y = self.waypoints[self.waypoint_index]

        if self.change_timer_1 <= 0:
            self.bullet_set_pattern(random.randint(0, 3))
            self.bullet_freq = random.choice([0, 1, 4, 5, 3])
            self.bullet_set_freq()
            self.change_timer_1 = self.change_timer_1_init / 2

        dx = target_x - self.x
        dy = target_y - self.y
        angle = math.atan2(dy, dx)
        self.x += self.SPD * math.cos(angle)
        self.y += self.SPD * math.sin(angle)


class Bullet:
    def __init__(self):
        # Const.
        self.SPR = BULLETS_SPRITES
        # Var.
        self.spd = 8
        self.hitbox_x = 3
        self.hitbox_y = 0
        self.width = 7
        self.height = 11
        self.x = 0
        self.y = 0
        self.hsp = 0
        self.vsp = 0
        self.damage = 1
        self.current_frame = 3
        self.is_homing = False
        self.angle = 0
        # False - player's bullet, True - deals damage to player
        self.is_hazard = False
        self.bullet_type = 0

    def set_vars(self, hitbox_x, hitbox_y, width, height, spd):
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
        self.width = width
        self.height = height
        self.spd = spd

    def check_type(self):
        if self.bullet_type == 0 or self.bullet_type == 3:
            # player's small bullets
            self.set_vars(3, 0, 7, 11, 8)
        elif self.bullet_type == 2 or self.bullet_type == 4:
            # player's big bullets
            self.set_vars(0, 0, 13, 11, 8)
        elif self.bullet_type == 1:
            # small enemy bullet
            self.set_vars(1, 1, 5, 5, 4)

    def set_frame(self):
        if self.is_hazard == 0:
            if psl[0] in range(0, 31):
                self.current_frame = 3
            elif psl[0] in range(32, 79):
                self.current_frame = 4
            elif psl[0] in range(80, 127):
                if self.is_homing:
                    self.current_frame = 5
                else:
                    self.current_frame = 4
            elif psl[0] in range(128, 132):
                if self.is_homing:
                    self.current_frame = 6
                else:
                    self.current_frame = 4
        else:
            self.current_frame = 0

    def make_move(self):
        if self.is_homing:
            self.x += self.spd * 1.5 * math.cos(self.angle)
            self.y += self.spd * 1.5 * -math.sin(self.angle)
        else:
            self.x += self.hsp
            self.y += self.vsp

    def destroy_cond(self):
        if out_of_bounds(self):
            bullet_list.remove(self)
            del self


# bruh nwm co ja tu zrobilemxddd
def create_bullet(x, y, is_hazard, is_homing, move_to_x, move_to_y, bullet_type, angle_offset, consider_spd):
    bullet = Bullet()
    bullet.x, bullet.y = x - bullet.width / 2, y
    bullet.is_hazard = is_hazard
    bullet.vsp = -bullet.spd
    bullet.is_homing = is_homing
    if consider_spd:
        bullet.angle = calc_angle_spd(bullet.x, bullet.y, move_to_x, move_to_y, bullet.spd) + math.radians(angle_offset)
    else:
        bullet.angle = calc_angle(bullet.x, bullet.y, move_to_x, move_to_y) + math.radians(angle_offset)
    bullet.bullet_type = bullet_type
    bullet.check_type()
    bullet_list.append(bullet)
    return bullet


class Effect:
    def __init__(self):
        # Const.
        self.SPR = FX_SPRITES
        self.WIDTH = 1
        self.HEIGHT = 1
        # Var.
        # 0 - end anim after last frame, 1 - continue animating
        self.behaviour = 0
        # 0 - player's bullet destruction, 1 - enemy destruction
        self.type = 0
        self.anim_spd = 0.1
        self.x = 0
        self.y = 0
        self.hsp = 0
        self.vsp = 0
        self.current_frame = 0
        self.curr_anim_no_of_frs = 1
        self.angle = 0

    def set_init_frame(self):
        if self.type == 0:
            self.current_frame = 0
            self.curr_anim_no_of_frs = 4
        elif self.type == 1:
            self.current_frame = 5
            self.curr_anim_no_of_frs = 3 + self.current_frame

    def set_frame(self):
        self.current_frame += self.anim_spd
        if self.current_frame >= self.curr_anim_no_of_frs + 0.9:
            if self.behaviour == 0:
                self.destroy()

    def make_move(self):
        self.x += self.hsp * math.cos(self.angle)
        self.y += self.vsp * -math.sin(self.angle)

    def destroy(self):
        fx_list.remove(self)
        del self


class Powerup:
    def __init__(self):
        # Const.
        self.SPD = 2
        self.SIZE = 12
        # Var.
        self.x = 0
        self.y = 0
        self.hsp = 0
        self.vsp = 0
        self.friction = 0

    def set_vars(self):
        self.friction = random.uniform(0.01, 0.1)
        self.hsp = random.uniform(-2, 2)
        self.vsp = random.uniform(-2, -4)

    def make_move(self):
        self.hsp -= self.friction * numpy.sign(self.hsp)
        self.vsp += self.friction
        if self.vsp > 1.8:
            self.vsp = 1.8
        if abs(self.hsp) < 0.1:
            self.hsp = 0
        self.x += self.hsp
        self.y += self.vsp

    def collect(self):
        psl[0] += 1
        powerup_list.remove(self)
        del self

    def destroy_cond(self):
        if self.y > RESOLUTION[1] + 16:
            powerup_list.remove(self)
            del self


def create_powerup(x, y):
    powerup = Powerup()
    powerup.x, powerup.y = x - powerup.SIZE / 2, y - powerup.SIZE / 2
    powerup.set_vars()
    powerup_list.append(powerup)
    return powerup


class Background:
    def __init__(self):
        self.SPR = BG_SPRITES
        self.SPD = 0.5
        self.HEIGHT = 9696
        self.frame = 0
        self.y = -self.HEIGHT + 480

    def make_scroll(self, bg1):
        self.y += self.SPD

    def set_frame(self, frame):
        self.frame = frame
