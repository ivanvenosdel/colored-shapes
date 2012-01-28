import pygame
from pygame.locals import *

class Control:
    def __init__(self):
        self.moverate = 5
        self.moveLeft  = False
        self.moveRight = False
        self.moveUp    = False
        self.moveDown  = False          
 
    def update(self, event):
        if event.type == KEYDOWN:
            if event.key in (K_UP, K_w):
                self.moveDown = False
                self.moveUp = True
            elif event.key in (K_DOWN, K_s):
                self.moveUp = False
                self.moveDown = True
            elif event.key in (K_LEFT, K_a):
                self.moveRight = False
                self.moveLeft = True
            elif event.key in (K_RIGHT, K_d):
                self.moveLeft = False
                self.moveRight = True
            
        elif event.type == KEYUP:
            # stop moving the player's squirrel
            if event.key in (K_LEFT, K_a):
                self.moveLeft = False
            elif event.key in (K_RIGHT, K_d):
                self.moveRight = False
            elif event.key in (K_UP, K_w):
                self.moveUp = False
            elif event.key in (K_DOWN, K_s):
                self.moveDown = False