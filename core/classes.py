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

    def shoot_bullet(self):
        if self.keys[pygame.K_z]:
            if self.can_shoot is True:
                create_bullet(self.x + self.WIDTH/2, self.y, False, False, 0, 0, 0)
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
        self.SPD = 2.5
        self.WIDTH = 32
        self.HEIGHT = 32
        self.HITBOX_X = 13
        self.HITBOX_Y = 25
        self.HITBOX_SIZE = 8
        self.BULLET_HITBOX_X = 0
        self.BULLET_HITBOX_Y = 0
        self.ANIM_SPD = 0.15
        # Var.
        self.bullet_shooting_freq = 20
        self.current_frame = 0
        self.curr_anim_no_of_frs = 3
        self.can_move = True
        self.is_moving = False
        self.move_pattern = 0
        self.bullet_type = 1
        self.x = 180
        self.y = 170
        self.hsp = 0
        self.vsp = 0
        self.can_shoot = True
        self.bullet_clock = 0
        self.health = 1
        self.score_on_kill = 100

    def set_frame(self):
        self.current_frame += self.ANIM_SPD
        if self.current_frame >= self.curr_anim_no_of_frs + 0.9:
            self.current_frame = 0

    def shoot_bullet(self, to_x, to_y, bullet_type):
        if self.can_shoot is True:
            create_bullet(self.x + self.WIDTH/2, self.y + self.HEIGHT/2, True, True, to_x, to_y, bullet_type)
            self.can_shoot = False

        if self.can_shoot is False:
            self.bullet_clock += 1
            if self.bullet_clock > self.bullet_shooting_freq:
                self.bullet_clock = 0
                self.can_shoot = True

    def check_vitals(self):
        if self.health <= 0:
            self.destroy()

    def destroy(self):
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
        self.bullet_shooting_freq = 40
        self.bullet_type = 0


class FairyBlue(FairyRed):
    def __init__(self):
        super().__init__()
        self.SPR = BLUE_FAIRY_SPRITES
        self.health = 5
        self.bullet_type = 0
        self.bullet_shooting_freq = 20


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
        if self.bullet_type == 0:
            self.set_vars(3, 0, 7, 11, 8)
        elif self.bullet_type == 1:
            self.set_vars(1, 1, 5, 5, 4)

    def set_frame(self):
        if self.is_hazard == 0:
            if psl[0] > 16:
                self.current_frame = 4
            else:
                self.current_frame = 3
        else:
            self.current_frame = 0

    def make_move(self):
        if self.is_homing:
            self.x += self.spd * math.cos(self.angle)
            self.y += self.spd * -math.sin(self.angle)
        else:
            self.x += self.hsp
            self.y += self.vsp

    def destroy_cond(self):
        if out_of_bounds(self):
            bullet_list.remove(self)
            del self


# bruh nwm co ja tu zrobilemxddd
def create_bullet(x, y, is_hazard, is_homing, move_to_x, move_to_y, bullet_type):
    bullet = Bullet()
    bullet.x, bullet.y = x - bullet.width / 2, y
    bullet.is_hazard = is_hazard
    bullet.vsp = -bullet.spd
    bullet.is_homing = is_homing
    bullet.angle = calc_angle(bullet.x, bullet.y, move_to_x, move_to_y)
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
        if self.vsp > 2:
            self.vsp = 2
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
