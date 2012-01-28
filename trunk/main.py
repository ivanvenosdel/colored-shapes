import pygame
from pygame import surface
from pygame.locals import *

from actors import Octagon
from ui.Countdown import CountDown
from ui.Scoreboard import Scoreboard
from control import Control

from logic import Logic
from graphics import Graphics
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

        # Create empty background
        self.background = imageutils.load_image("BG_1.png")[0].convert()
        
        pygame.mouse.set_visible(1)
        
    # Continuesly renders the boid swarm
    def game_loop(self):
        clock = pygame.time.Clock()
        do_continue = True

        #Initialize
        self.scoreboard = Scoreboard()
        self.timer = CountDown()
        self.control = Control()
        #TEMP
        self.player = Octagon()
        self.player2 = Octagon()
        self.player2.rect.move_ip((150, 150))
        shape_layer = pygame.sprite.RenderPlain((self.player, self.player2))    
        #ENDTEMP        
        self.logic = Logic(self.player, self.scoreboard, self.timer, self.control)
        #self.graphics = Graphics(self.player, self.scoreboard, self.timer);
        
          
        # Render the boid swarm
        while do_continue:
            delta = clock.tick(30) # fps

            # Catch input event
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                else:
                    self.control.update(event)
            
            #TEMP
            shape_layer.update(delta)            
            #ENDTEMP                     
                       
            # Update 
            self.logic.update(delta)
            
            # Render    
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.scoreboard.image, (0, 0))
            self.screen.blit(self.timer.image, (150, 0))
            
            shape_layer.draw(self.screen)            
            pygame.display.flip()        
        
def main():
    view = Shapescape()

    # End game
    pygame.quit()
    
#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
