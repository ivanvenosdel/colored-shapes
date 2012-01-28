import pygame
from pygame import surface
from pygame.locals import *

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
        # Prepary to loop
        clock = pygame.time.Clock()
        do_continue = True
        SCORE = Scoreboard()
        
        # Render the boid swarm
        while do_continue:
            clock.tick(30) # fps

            # Catch input event
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            
            # Update screen
            self.screen.blit(self.background, (0,0))
            self.screen.blit(SCORE.image, (0, 0))
            SCORE.update()
            pygame.display.flip()        
        
class Scoreboard:
    def __init__(self):
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('white')
        self.lastscore = -1
        self.currentscore = 0
        self.update()
        self.rect = self.image.get_rect().move(0, 450)
        
        
    def update(self):
        if self.currentscore != self.lastscore:
            self.lastscore = self.currentscore
            msg = "Score: %d" % self.currentscore
            self.image = self.font.render(msg, 0, self.color)
            

    
def main():
    view = Shapescape()
    
    # End game
    pygame.quit()
    
#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
