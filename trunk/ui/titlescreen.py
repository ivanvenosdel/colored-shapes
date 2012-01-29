import pygame
from pygame.locals import *

import os

import imageutils

class TitleScreen():
    def __init__(self, screen):
        self.screen = screen
        self.background = imageutils.load_image("title_screen.png")[0].convert()  
        self.music = os.path.join('data', "music.wav")
        
    def do_loop(self):
        
        #Loop until the user clicks the close button.
        done=False
  
        # Used to manage how fast the screen updates
        clock=pygame.time.Clock()
  
        pygame.mixer.Sound(self.music).play(-1)
        
        while done==False:  
            for event in pygame.event.get(): # User did something
                if event.type == KEYDOWN: # If user clicked close
                     if event.key is (K_RETURN):
                        done=True # Flag that we are done so we exit this loop
            self.screen.blit(self.background, (0,0)) 
            pygame.display.flip() 
            
            
