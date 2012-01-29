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

from ui.titlescreen import TitleScreen



class Shapescape:
    # Initialize the boid view
    def __init__(self):
        self.win_width = 1024
        self.win_height = 768
        pygame.init()
        self.init_window()
        title_screen = TitleScreen(self.screen)
        title_screen.do_loop()
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
        self.graphics = Graphics(self.scoreboard, self.timer);
        self.player = Player(self.graphics)
        self.world = World(self.graphics, self.player) 
        self.logic = Logic(self.player, self.world, self.scoreboard, self.timer, self.control)
        
        #TEMP
        #shape1 = self.world.create_shape("tri", 64, 0, "red")
        #shape2 = self.world.create_shape("octagon", 64, 0, "blue")
        #shape3 = self.world.create_shape("square", 64, 0, "red")
        #shape4 = self.world.create_shape("tri", 64, 0, "blue")
        #self.player.attach_shape(shape1)
        #self.player.attach_shape(shape2)
        #self.player.attach_shape(shape3)
        #self.player.attach_shape(shape4)
        #ENDTEMP
        
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
            self.graphics.update(self.screen, delta)
            
            # Render
            self.graphics.draw(self.screen, delta);
              
            pygame.display.flip()        
        
def main():
    view = Shapescape()

    # End game
    pygame.quit()
    
#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
