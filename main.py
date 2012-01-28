import pygame
from pygame import surface
from pygame.locals import *
from actors import Octagon
from ui.Countdown import CountDown
from ui.Scoreboard import Scoreboard
from control import Control

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
        SCORE = Scoreboard()
        Timer = CountDown()
        shape = Octagon()

        control = Control()
        shape_layer = pygame.sprite.RenderPlain((shape))      

        
        # Render the boid swarm
        while do_continue:
            delta = clock.tick(30) # fps
            Timer.Milli -= delta;

            # Catch input event
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                else:
                    control.update(event)
                              
        
            # Update 
            shape_layer.update(delta)
            if control.moveLeft:
                shape.rect.move_ip(-control.moverate, 0)
            if control.moveRight:
                shape.rect.move_ip(control.moverate, 0)
            if control.moveUp:
                shape.rect.move_ip(0, -control.moverate)
            if control.moveDown:
                shape.rect.move_ip(0, control.moverate)            
            
            
            # Render    
            self.screen.blit(self.background, (0,0))
            self.screen.blit(SCORE.image, (0, 0))
            self.screen.blit(Timer.image, (150, 0))
            SCORE.update()
            Timer.update()
            
            shape_layer.draw(self.screen)            
            pygame.display.flip()        
        
def main():
    view = Shapescape()

    # End game
    pygame.quit()
    
#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
