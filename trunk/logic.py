import pygame
from pygame import sprite

from vector2 import Vector2
from actors import Head

class Logic:
    def __init__(self, player, world, scoreboard, timer, control):
        self.player = player
        self.world = world
        self.scoreboard = scoreboard
        self.timer = timer
        self.control = control
        self.playerspeed = 10
        
        self.driftx = 0
        self.drifty = 0
        
    def update(self, delta):
        #Move player shapes from last head move
        for shape in self.player.get_render_list():
            if type(shape) is not Head:
                if shape.parent.last_vector:
                    shape.rect.move_ip(shape.parent.last_vector.x, shape.parent.last_vector.y)
        
        #Handle Input
        if self.control.rotateLeft and self.control.moveUp:
            self.player.head.rotation = (self.player.head.rotation + 5) %360
            self.player.head.rotate_direction(self.player.head.rotation)
        elif self.control.rotateRight and self.control.moveUp:
            self.player.head.rotation = (self.player.head.rotation - 5) %360
            self.player.head.rotate_direction(self.player.head.rotation)
        if self.control.moveUp:
            self.driftx = self.player.head.directionx*self.playerspeed
            self.drifty = -self.player.head.directiony*self.playerspeed
            self.player.head.rect.move_ip(self.driftx, self.drifty)
        elif self.driftx != 0 or self.drifty != 0:
            if self.driftx > 0:
                self.driftx -= 1
                if self.driftx < 0:
                    self.driftx = 0
            elif self.driftx < 0:
                self.driftx += 1
                if self.driftx > 0:
                    self.driftx = 0
                
            if self.drifty > 0:
                self.drifty -= 1
                if self.drifty < 0:
                    self.drifty = 0                
            elif self.drifty < 0:
                self.drifty += 1  
                if self.drifty > 0:
                    self.drifty = 0       
         
            self.player.head.rect.move_ip(self.driftx, self.drifty)
            
        #Update Countdown Timer
        self.timer.Milli -= delta
        self.timer.update()        

        #Update score value
        self.scoreboard.update()
        
        #Collisions
        for player_piece in self.player.get_render_list():
                for enemy in self.world.enemies.values():
                    if player_piece.bounding.colliderect(enemy.bounding):
                        if self.player.total_size >= enemy.size or enemy.size == 20:
                            if type(player_piece) is Head:
                                self.world.remove_enemy(enemy.id)
                                self.player.attach_shape(enemy)
                                self.timer.add_seconds(15)
                                self.scoreboard.plusscore(enemy.pointvalue)
                        else:
                            self.player.kill_shape(player_piece)
                            return
                        break #do one collision per shape a frame
                    
        
        
      
    
    