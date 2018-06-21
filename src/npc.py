import pygame
import sys

sys.path.insert(0, 'src/managers/')

import asset_manager
import desc_manager
import time

#TODO, have them stay still and move with the houses to look as though standing still

class NPC:

    def __init__(self, position, image, in_grass, group):
        self.spritesheet = image
        self.position = [0, 0]
        self.position_offset = position
        self.group = group
        self.in_grass = in_grass

        self.img_rect = (0, 0, 0, 0)

        # Rounds the position to every 4 pixels.
        self.pos = (round(self.position[0] / 4) * 4, round(self.position[1] / 4) * 4)

        if self.in_grass == True:
            self.img_rect = (0, self.group * 20, 16, 11)
        else:
            self.img_rect = (0, self.group * 20, 16, 20)

        self.cut_img = self.spritesheet.subsurface(self.img_rect)
        self.cut_img = pygame.transform.scale(self.cut_img, (self.cut_img.get_width() * 4, self.cut_img.get_height() * 4))

    def get_offset(self, offset):
        # 0 == translate, 1 = set_pos
        if offset[0] == 0:
            self.position[0] += offset[1]
            self.position[1] += offset[2]
        else:
            self.position[0] = offset[1]
            self.position[1] = offset[2]

    def walk_left(self, group1, group2):

        #TODO, needs to pause in between animations

        self.img_rect = (0, group1 * 20, 16, 20)
        self.cut_img = self.spritesheet.subsurface(self.img_rect)
        self.cut_img = pygame.transform.scale(self.cut_img, (self.cut_img.get_width() * 4, self.cut_img.get_height() * 4))
        self.position_offset[0] -= 64

        self.img_rect = (0, group2 * 20, 16, 20)
        self.cut_img = self.spritesheet.subsurface(self.img_rect)
        self.cut_img = pygame.transform.scale(self.cut_img, (self.cut_img.get_width() * 4, self.cut_img.get_height() * 4))
        self.position_offset[0] -= 64

        self.img_rect = (0, self.group * 20, 16, 20)
        self.cut_img = self.spritesheet.subsurface(self.img_rect)
        self.cut_img = pygame.transform.scale(self.cut_img, (self.cut_img.get_width() * 4, self.cut_img.get_height() * 4))
        self.position_offset[0] -= 64


    def draw(self, surface):

        surface.blit(self.cut_img, (self.position[0] + self.position_offset[0], self.position[1] + self.position_offset[1]))
