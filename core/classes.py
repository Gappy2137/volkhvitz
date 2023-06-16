"""Classes."""
from imports import *


class Player:
    def __init__(self):
        # Const.
        self.SPD = 3
        self.WIDTH = 32
        self.HEIGHT = 48
        self.HITBOX_X = 13
        self.HITBOX_Y = 25
        self.HITBOX_SIZE = 8
        self.ANIM_SPD = 0.15
        self.DIAG_MULTIPLIER = 0.75
        self.FOCUS_MULTIPLIER = 0.5
        self.BULLET_SHOOTING_FREQ = 2
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
                self.hsp *= self.FOCUS_MULTIPLIER
                self.vsp *= self.FOCUS_MULTIPLIER

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
                bul = Bullet()
                bul.vsp = -bul.SPD
                bul.x = self.x + self.WIDTH/2 - bul.width/2
                bul.y = self.y
                bul.type = 0
                bullet_list.append(bul)
                self.can_shoot = False
        else:
            self.can_shoot = True

        if self.can_shoot is False:
            self.bullet_clock += 1
            if self.bullet_clock > self.BULLET_SHOOTING_FREQ:
                self.bullet_clock = 0

        if self.bullet_clock == 0:
            self.can_shoot = True


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
        self.BULLET_SHOOTING_FREQ = 10
        # Var.
        self.current_frame = 0
        self.curr_anim_no_of_frs = 3
        self.can_move = True
        self.is_moving = False
        self.move_pattern = 0
        self.bullet_type = 0
        self.x = 180
        self.y = 170
        self.hsp = 0
        self.vsp = 0
        self.can_shoot = True
        self.bullet_clock = 0

    def set_frame(self):
        self.current_frame += self.ANIM_SPD
        if self.current_frame >= self.curr_anim_no_of_frs + 0.9:
            self.current_frame = 0

    def shoot_bullet(self):
        if self.can_shoot is False:
            self.bullet_clock += 1
            if self.bullet_clock > self.BULLET_SHOOTING_FREQ:
                self.bullet_clock = 0
                self.can_shoot = True

        if self.keys[pygame.K_z]:
            if self.can_shoot is True:
                bul = Bullet()
                bul.vsp = -bul.SPD
                bul.x = self.x + self.WIDTH/2 - bul.width/2
                bul.y = self.y
                bullet_list.append(bul)
                self.can_shoot = False


class FairyRed(Enemy):
    def __init__(self):
        super().__init__()
        self.SPR = RED_FAIRY_SPRITES
        self.WIDTH = 32
        self.HEIGHT = 32
        self.HITBOX_X = 10
        self.HITBOX_Y = 11
        self.HITBOX_SIZE = 12


class FairyBlue(FairyRed):
    def __init__(self):
        super().__init__()
        self.SPR = BLUE_FAIRY_SPRITES


class Bullet:
    def __init__(self):
        # Const.
        self.SPR = BULLETS_SPRITES
        self.SPD = 8
        self.HEIGHT = 11
        self.HITBOX_Y = 0
        # Var.
        self.x = 0
        self.y = 0
        self.hsp = 0
        self.vsp = 0
        self.damage = 1
        self.width = 7
        self.hitbox_x = 3
        self.current_frame = 3
        # 0 - player bullet 1 - enemy bullet
        self.type = 0

    def set_frame(self):
        if self.type == 0:
            if power > 16:
                self.current_frame = 4
            else:
                self.current_frame = 3
        else:
            self.current_frame = 0

    def make_move(self):
        self.x += self.hsp
        self.y += self.vsp

    def destroy_cond(self):
        if 0 > self.y > RESOLUTION[1]:
            bullet_list.pop(0)
            del self


class Powerup:
    def __init__(self):
        # Const.
        self.SPD = 2
        self.WIDTH = 12
        self.HEIGHT = 12
        self.HITBOX_X = 0
        self.HITBOX_Y = 0
        self.HITBOX_SIZE = 12
        # Var.
        self.x = 0
        self.y = 0
        self.hsp = 0
        self.vsp = 0
