import pygame.gfxdraw
import pygame.surface
import pygame.color
from pygame.locals import *
from pygame.color import *

class Shapescape:
    # Initialize the boid view
    def __init__(self):
        self.winWidth = 1024
        self.winHeight = 768
        
        pygame.init()
        self.initWindow()
        self.gameLoop()
    
    # Prepares the boid view
    def initWindow(self): 
        # Initialize window
        self.screen = pygame.display.set_mode((self.winWidth, self.winHeight))
        pygame.display.set_caption('Shapescape')

        # Create empty background
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((0, 0, 0))
        
        pygame.mouse.set_visible(1)
        
    # Continuesly renders the boid swarm
    def gameLoop(self):
        # Prepary to loop
        clock = pygame.time.Clock()
        doContinue = True

        # Render the boid swarm
        while doContinue:
            clock.tick(30) # fps

            # Catch input event
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                #elif event.type == MOUSEBUTTONDOWN:
                    #pos = pygame.mouse.get_pos()

                    ## Set target position
                    #if pygame.mouse.get_pressed()[0] == 1:                   
                        #if self.target is not None:
                            #self.targetRenderGroup.remove(self.target)
                        #self.target = Target(pos[0], pos[1])
                        #self.boidSwarm.target = Vector2D(pos[0], pos[1])
                        #self.targetRenderGroup.add(self.target)
                        
                    ## Set obstacle position
                    #if pygame.mouse.get_pressed()[2] == 1:                   
                        #if self.obstacle is not None:
                            #self.obstacleRenderGroup.remove(self.obstacle)
                        #self.obstacle = Target(pos[0], pos[1], 10, 10, 'red')
                        #self.boidSwarm.obstacle = Vector2D(pos[0], pos[1])

                        #self.obstacleRenderGroup.add(self.obstacle)                        

            
            # Update screen
            self.screen.blit(self.background, (0,0))
            pygame.display.flip()        
        
        
def main():
    view = Shapescape()

    # End game
    pygame.quit()
    
#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
