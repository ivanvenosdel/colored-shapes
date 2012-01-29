import uuid
import math
import string

import pygame
from pygame.sprite import Sprite
import actors
from actors import *
import imageutils

from vector2 import Vector2

class Shape(Sprite):
    loaded_images = {}

    def __init__(self, texture_path, size, rotation, shape_type, color):
        Sprite.__init__(self) #call Sprite intializer
        self.id = uuid.uuid1()
        
        self.rotation = rotation
        self.size = size
        self.texture_path = texture_path
        self.color = color
        
        self.image = pygame.transform.scale(self.getfile(self.texture_path), (self.size, self.size))
        self.rect = self.image.get_rect();
        
        self.original = self.image;
        
        self.bounding = self.rect.inflate(-self.rect.width/2.25, -self.rect.height/2.25)      
        self.pointvalue = 0
        if shape_type == actors.Octagon.shape_type:
            self.pointvalue = 800
        elif shape_type == actors.Hexagon.shape_type:
            self.pointvalue = 800
        elif shape_type == actors.Pentagon.shape_type:
            self.pointvalue = 500
        elif shape_type == actors.Square.shape_type:
            self.pointvalue = 400
        elif shape_type == actors.Tri.shape_type:
            self.pointvalue = 300
            
        self.directionx = 1
        self.directiony = 0
        
        self.last_location = None
        self.last_vector = None
        self.parent = None
        
        self.randirx = 0
        self.randiry = 0
        
    def update(self, delta):
        if self.last_location:
            self.last_vector = Vector2.from_points(self.last_location, (self.rect.x, self.rect.y))
        
        self.rect.move_ip((self.randirx, self.randiry))
        
        center = self.rect.center
        self.image = pygame.transform.rotate(self.original, self.rotation)
        self.rect = self.image.get_rect(center=center)
        self.bounding = self.rect.inflate(-self.rect.width/2.25, -self.rect.height/2.25) 
        
        self.last_location = (self.rect.x, self.rect.y)
        
        
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
        x = cos
        y = sin
        self.directionx = x
        self.directiony = y