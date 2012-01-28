import pygame
from pygame import surface
from pygame.locals import *

from actors import Octagon
from ui.Countdown import CountDown
from ui.Scoreboard import Scoreboard
from control import Control
from logic import Logic
from graphics import Graphics
from world import World
from player import Player

import imageutils

class Shapescape:
    # Initialize the boid view
    def __init__(self):
        self.win_width = 1024
        self.win_height = 768
        
        pygame.init()
        self.init_window()
        self.game_loop()
    
    # Prepares the boid view
    def init_window(self): 
        # Initialize window
        self.screen = pygame.display.set_mode((self.win_width, self.win_height))
        pygame.display.set_caption('Shapescape')

        pygame.mouse.set_visible(1)
        
    # Continuesly renders the boid swarm
    def game_loop(self):
        clock = pygame.time.Clock()
        do_continue = True

        #Initialize
        self.scoreboard = Scoreboard()
        self.timer = CountDown()
        self.control = Control()
        self.world = World()
        self.player = Player()
        self.logic = Logic(self.player, self.scoreboard, self.timer, self.control)
        self.graphics = Graphics(self.player, self.world, self.scoreboard, self.timer);
        
        while do_continue:
            delta = clock.tick(30) # fps

            # Catch input event
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                else:
                    self.control.update(event)
                
            # Update 
            self.logic.update(delta)
            self.world.update(delta)
            self.graphics.update(delta)
            
            # Render
            self.graphics.draw(self.screen, delta);
                     
            pygame.display.flip()        
        
def main():
    view = Shapescape()

    # End game
    pygame.quit()
    
#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
