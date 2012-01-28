import random
import uuid

import pygame
from pygame.sprite import Sprite

import imageutils

class Head(Sprite):
    
    def __init__(self):
        Sprite.__init__(self) #call Sprite intializer
        
        self.id = uuid.uuid1()
        self.texture_path = "head.png"
        self.original, self.rect = imageutils.load_image(self.texture_path, -1)
        
        #Make origin the center of the shape
        self.rect = self.original.get_rect(center=self.rect.center)
        
        self.rect.move_ip((-self.original.get_width()/2, -self.original.get_height()/2))
        
        self.image = pygame.transform.scale(self.original, (64,64))
        self.rect = self.image.get_rect()
        
    def update(self, delta):
        pass
        
    