"""Classes."""
from imports import *


class Player:
    def __init__(self):
        # Const.
        self.SPD = 3.0
        self.WIDTH = 32
        self.HEIGHT = 48
        self.HITBOX_X = 13
        self.HITBOX_Y = 25
        self.HITBOX_SIZE = 8
        self.ANIM_SPD = 0.15
        # Var.
        self.keys = []
        self.current_frame = 0
        self.curr_anim_no_of_frs = 1
        self.can_move = True
        self.is_moving = False
        self.x = 200
        self.y = 200
        self.hsp = 0
        self.vsp = 0

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
                self.vsp = self.SPD
            elif self.keys[pygame.K_UP] and not self.keys[pygame.K_DOWN]:
                self.vsp = -self.SPD
            else:
                self.vsp = 0

            if self.keys[pygame.K_LEFT] and not self.keys[pygame.K_RIGHT]:
                self.hsp = -self.SPD
            elif self.keys[pygame.K_RIGHT] and not self.keys[pygame.K_LEFT]:
                self.hsp = self.SPD
            else:
                self.hsp = 0

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
