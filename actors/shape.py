import random

import pygame
from pygame.sprite import Sprite

import imageutils

class Shape(Sprite):
    def __init__(self, shape, color):
        Sprite.__init__(self) #call Sprite intializer

        self.color = color
        self.shape = shape
        self.texture_path = "%s_%s.png" % (color, self.shape)
        self.image, self.rect = imageutils.load_image(self.texture_path, -1)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.move_ip((-self.image.get_width()/2, -self.image.get_height()/2))
        self.small = pygame.transform.scale(self.image, (64,64))
        
        self.rotation = 0;

    def update(self, delta):
        self.rotation = (self.rotation + 5) % 360
        center = self.rect.center
        self.image = pygame.transform.rotate(self.small, self.rotation)
        self.rect = self.image.get_rect(center=center)
