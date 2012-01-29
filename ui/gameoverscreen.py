import pygame
from pygame.locals import *

import os

import imageutils

class GameOver():
    def __init__(self, screen):
        self.screen = screen
        self.background = imageutils.load_image("BG_gameover.png")[0].convert()  
        
    def do_loop(self):
        
        #Loop until the user clicks the close button.
        done=False
  
        # Used to manage how fast the screen updates
        clock=pygame.time.Clock()
        
        while done==False:  
            for event in pygame.event.get(): # User did something
                if event.type == KEYDOWN: # If user clicked close
                     if event.key is (K_ESCAPE):
                        done=True # Flag that we are done so we exit this loop
            self.screen.blit(self.background, (0,0)) 
            pygame.display.flip() 