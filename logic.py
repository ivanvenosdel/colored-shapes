import pygame
from pygame import sprite

from vector2 import Vector2
from actors import Head
import globalvars

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
        self.player.update(delta)
        
        #ONLY move the shapes attached to head and not far
        for shape in self.player.get_render_list():
            if type(shape) is not Head:
                if type(shape.parent) is not Head:
                    if shape.parent.last_vector:
                        shape.rect.move_ip(shape.parent.last_vector.x, shape.parent.last_vector.y)
                else:
                    #Only the people following head
                    head = shape.parent
                    shape.rect.move_ip(-head.directionx*(head.rect.width /2 + shape.rect.width /2), -head.directiony*(head.rect.height /2 + shape.rect.height /2))
        
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
            #self.player.head.rect.move_ip(self.driftx, self.drifty)
            globalvars.GLOBAL_DELTA_X = self.driftx
            globalvars.GLOBAL_DELTA_Y = self.drifty
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
               
            globalvars.GLOBAL_DELTA_X = self.driftx
            globalvars.GLOBAL_DELTA_Y = self.drifty
            
            #self.player.head.rect.move_ip(self.driftx, self.drifty)
            
        if globalvars.GLOBAL_DELTA_X != 0 or globalvars.GLOBAL_DELTA_Y != 0: 
            #update ai positions
            for enemy in self.world.enemies.values():
                enemy.rect.move_ip(-globalvars.GLOBAL_DELTA_X, -globalvars.GLOBAL_DELTA_Y)
            
        #Update Countdown Timer
        self.timer.Milli -= delta
        self.timer.update()
        if self.timer.Milli <= (0):
            pygame.quit()
            

        #Update score value
        self.scoreboard.update()
        
        #Collisions
        if not self.player.invincible:
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
                                self.world.add_enemy_shape(player_piece)
                                self.player.invincible = True
                                self.player.invincible_timer = self.player.invincible_rate
                                return
                            break #do one collision per shape a frame

                    
        
        
      
    
    