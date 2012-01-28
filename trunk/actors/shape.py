import pygame
from pygame.sprite import Sprite

import imageutils

class Shape(Sprite):
    def __init__(self):
        Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = imageutils.load_image('blue_octagon.png', -1)
        self.rect.topleft = 80, 10



    
    def update(self):
        pass 
