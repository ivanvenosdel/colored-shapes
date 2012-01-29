import random
import uuid
import math

import pygame
from pygame.sprite import Sprite

import imageutils

class Shape(Sprite):
    loaded_images = {}

    def __init__(self, texture_path, size, rotation):
        Sprite.__init__(self) #call Sprite intializer
        self.id = uuid.uuid1()
        
        self.rotation = rotation
        self.size = size
        self.texture_path = texture_path
        
        self.image = pygame.transform.scale(self.getfile(self.texture_path), (self.size, self.size))
        self.rect = self.image.get_rect();
        self.original = self.image;
        self.directionx = 1
        self.directiony = 0
        
    def update(self, delta):
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
        
    @classmethod
    def build_texture_path(self, color, shape_type):
        return "%s_%s.png" % (color, shape_type)
        
    def rotate_direction(self, angle_degrees):
        radians = math.radians(angle_degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        #x = self.directionx*cos - self.directiony*sin
        #y = self.directionx*sin + self.directiony*cos
        x = cos
        y = sin
        self.directionx = x
        self.directiony = y