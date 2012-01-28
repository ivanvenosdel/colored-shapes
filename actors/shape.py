import random
import uuid

import pygame
from pygame.sprite import Sprite

import imageutils

class Shape(Sprite):
    loaded_images = {}

    def __init__(self, shape, color):
        Sprite.__init__(self) #call Sprite intializer
        self.id = uuid.uuid1()
        self.color = color
        self.shape = shape
        self.texture_path = "%s_%s.png" % (color, self.shape)
        self.image = pygame.transform.scale(self.getfile(self.texture_path), (64,64))
        self.rect = self.image.get_rect();
        self.original = self.image;
        
        self.rotation = 0;

    def update(self, delta):
        self.rotation = (self.rotation + 5) % 360
        center = self.rect.center
        self.image = pygame.transform.rotate(self.original, self.rotation)
        self.rect = self.image.get_rect(center=center)
        
    def getfile(self, texture_path):
        if texture_path in Shape.loaded_images:
            return Shape.loaded_images[texture_path]
        else:
            image, rect = imageutils.load_image(texture_path, -1)
            rect = image.get_rect(center=rect.center)
            rect.move_ip((-image.get_width()/2, -image.get_height()/2))
            Shape.loaded_images[texture_path] = image
            return image