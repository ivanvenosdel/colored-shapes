import pygame

import imageutils

class Graphics:
    def __init__(self, player, world, scoreboard, timer):
        self.player = player
        self.world = world
        self.scoreboard = scoreboard
        self.timer = timer
        
        # Create empty background
        self.background = imageutils.load_image("BG_1.png")[0].convert()
        
        # Create Layers
        self.shape_layer = pygame.sprite.RenderPlain((self.player))    
        
    def update(self, delta):
        self.shape_layer.update(delta)         
    
    def draw(self, screen, delta):
        # Background base
        screen.blit(self.background, (0,0))
        
        # Draw the layers
        self.shape_layer.draw(screen)   
        
        # Draw UI
        screen.blit(self.scoreboard.image, (0, 0))
        screen.blit(self.timer.image, (940, 0))
        