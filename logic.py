import pygame
from pygame import sprite
from pygame.locals import *

from vector2 import Vector2
from actors import Head
import globalvars

import os
import imageutils

class Logic:
    def __init__(self, player, world, scoreboard, timer, control):
        self.player = player
        self.world = world
        self.scoreboard = scoreboard
        self.timer = timer
        self.control = control
        self.playerspeed = 10
        self.crash = os.path.join('data', "crash.wav")
        self.slurp = os.path.join('data', "slurp.wav")
        
        self.driftx = 0
        self.drifty = 0
        
    def update(self, delta):
        self.player.update(delta)
        
        #ONLY move the shapes attached to head and not far
        for shape in self.player.get_render_list():
            if type(shape) is not Head:
                if shape.parent.last_location:
                    head = shape.parent
                    shape.rect = head.rect.copy()
                    shape.rect.move_ip(-globalvars.GLOBAL_DELTA_X, -globalvars.GLOBAL_DELTA_Y)   
                    shape.rotatation = shape.parent.rotation
        
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
            
        if globalvars.GLOBAL_DELTA_X != 0 or globalvars.GLOBAL_DELTA_Y != 0: 
            #update ai positions
            for enemy in self.world.enemies.values():
                enemy.rect.move_ip(-globalvars.GLOBAL_DELTA_X, -globalvars.GLOBAL_DELTA_Y)
            
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
                                pygame.mixer.Sound(self.slurp).play()
                        elif not self.player.invincible:
                            player_piece = self.player.kill_shape(player_piece)
                            self.world.add_enemy_shape(player_piece)
                            self.player.invincible = True
                            self.player.invincible_timer = self.player.invincible_rate
                            pygame.mixer.Sound(self.crash).play()
                            return
                        break #do one collision per shape a frame

                    
        
        
      
    
    