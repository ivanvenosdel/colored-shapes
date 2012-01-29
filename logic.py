import pygame
from pygame import sprite

class Logic:
    def __init__(self, player, world, scoreboard, timer, control):
        self.player = player
        self.world = world
        self.scoreboard = scoreboard
        self.timer = timer
        self.control = control
        self.playerspeed = 10
        
    def update(self, delta):
        #Handle Input
        if self.control.rotateLeft and self.control.moveUp:
            self.player.head.rotation = (self.player.head.rotation + 5) %360
            self.player.head.rotate_direction(self.player.head.rotation)
        elif self.control.rotateRight and self.control.moveUp:
            self.player.head.rotation = (self.player.head.rotation - 5) %360
            self.player.head.rotate_direction(self.player.head.rotation)
        if self.control.moveUp:
            self.player.head.rect.move_ip(self.player.head.directionx*self.playerspeed, -self.player.head.directiony*self.playerspeed)
        
        #Test Collisions
        for player_piece in self.player.get_render_list():
            for enemy in self.world.enemies:
                if pygame.sprite.collide_circle(player_piece, enemy):
                    if player_piece.rect.size > enemy.rect.size:
                        self.player.attach_shape(enemy)
                    else:
                        pass
                    break #do one collision per shape a frame
                    
        #Update Countdown Timer
        self.timer.Milli -= delta
        self.timer.update()        

        #Update score value
        self.scoreboard.update()
        
      
    
    