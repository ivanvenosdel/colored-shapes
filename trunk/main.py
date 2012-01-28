import pygame
from pygame import surface
from pygame.locals import *
from actors.shape import Shape

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
        
        #Dudes
        self.monster = pygame.image.load("monster.png").convert_alpha()
        
        pygame.mouse.set_visible(1)
        
    # Continuesly renders the boid swarm
    def game_loop(self):
        clock = pygame.time.Clock()
        do_continue = True

        #TEMP
        monster_x_position = 0
        monster_y_position = 0
        #END TEMP
        shape = Shape()
        shape_layer = pygame.sprite.RenderPlain((shape))
        
        # Render the boid swarm
        while do_continue:
            clock.tick(30) # fps
            
            #TEMP
            monster_x_position += 5
            if monster_x_position > self.win_width:
                #Back to left
                monster_x_position -= self.win_width
                
            monster_y_position += 5
            if monster_y_position > self.win_height:
                #Back to top
                monster_y_position -= self.win_height
            #END TEMP

            # Catch input event
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            
            # Update 
            shape_layer.update()
            
            # Render    
            self.screen.blit(self.background, (0,0))
            shape_layer.draw(self.screen)            
            self.screen.blit(self.monster, (monster_x_position,monster_y_position))
            pygame.display.flip()        
        
def main():
    view = Shapescape()

    # End game
    pygame.quit()
    
#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
