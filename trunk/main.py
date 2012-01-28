import pygame
from pygame import surface
from pygame.locals import *
from actors import Octagon
from ui.Countdown import CountDown
from ui.Scoreboard import Scoreboard

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
        self.background = surface.Surface(self.screen.get_size()).convert()
        self.background.fill((0, 0, 0))
        
        pygame.mouse.set_visible(1)
        
    # Continuesly renders the boid swarm
    def game_loop(self):
        clock = pygame.time.Clock()
        do_continue = True
        SCORE = Scoreboard()
        Timer = CountDown()
        shape = Octagon()
        shape_layer = pygame.sprite.RenderPlain((shape))
        
        # Render the boid swarm
        while do_continue:
            Timer.Milli -= clock.tick(30) # fps

            # Catch input event
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            
            # Update 
            shape_layer.update()
            
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
