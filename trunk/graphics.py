import pygame

import imageutils


class Graphics:
    def __init__(self, scoreboard, timer):
        self.scoreboard = scoreboard
        self.timer = timer
        
        # Create empty background
        self.background = imageutils.load_image("BG_1.png")[0].convert()
        
        # Create Layers
        self.player_layer = pygame.sprite.RenderPlain()
        self.enemy_layer = pygame.sprite.RenderPlain()
        
    def update(self, screen, delta):
        self.player_layer.update(delta)
        self.enemy_layer.update(delta)
              
    def draw(self, screen, delta):
        # Background base
        screen.blit(self.background, (0,0))
        
        # Draw the Player
        self.player_layer.draw(screen)
        
        # Draw the enemies
        self.enemy_layer.draw(screen)

        # Draw UI
        screen.blit(self.scoreboard.image, (0, 0))
        screen.blit(self.timer.image, (940, 0))
    
    def add_player_shape(self, shape):
        self.player_layer.add(shape)
    
    def remove_player_shape(self, shape):
        if self.player_layer.has(shape):
            self.player_layer.remove(shape)
            
    def add_enemy_shape(self, shape):
        self.enemy_layer.add(shape)
    
    def remove_enemy_shape(self, shape):
        if self.enemy_layer.has(shape):
            self.enemy_layer.remove(shape)            
            