import pygame
from pygame.locals import *

class Control:
    def __init__(self):
        self.moverate = 5
        self.rotateLeft  = False
        self.rotateRight = False
        self.moveUp    = False         
 
    def update(self, event):
        if event.type == KEYDOWN:
            if event.key in (K_UP, K_w):
                self.moveUp = True
            elif event.key in (K_LEFT, K_a):
                self.rotateRight = False
                self.rotateLeft = True
            elif event.key in (K_RIGHT, K_d):
                self.rotateLeft = False
                self.rotateRight = True
            
        elif event.type == KEYUP:
            # stop moving the player's squirrel
            if event.key in (K_LEFT, K_a):
                self.rotateLeft = False
            elif event.key in (K_RIGHT, K_d):
                self.rotateRight = False
            elif event.key in (K_UP, K_w):
                self.moveUp = False
                