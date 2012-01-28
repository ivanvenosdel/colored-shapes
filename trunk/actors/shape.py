import pygame
from pygame.sprite import Sprite

import imageutils

class Shape(Sprite):
    def __init__(self, shape, color):
        Sprite.__init__(self) #call Sprite intializer
        self.color = color
        self.shape = shape
        self.texture_path = "../data/%s_%s.png" % (color, self.shape)
        self.image, self.rect = imageutils.load_image(self.texture_path, -1)
    
    def update(self):
        pass 
