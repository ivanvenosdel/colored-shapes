import pygame
from pygame import sprite
from pygame.locals import *

from vector2 import Vector2
from actors import Head
import globalvars
import world

import os
import imageutils

class Logic:
    def __init__(self, player, world, graphics, scoreboard, timer, control):
        self.player = player
        self.world = world
        self.scoreboard = scoreboard
        self.timer = timer
        self.control = control
        self.playerspeed = 10
        self.crash = os.path.join('data', "crash.wav")
        self.slurp = os.path.join('data', "slurp.wav")
        self.graphics = graphics
        
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
            deadenemies = []
            for enemy in self.world.enemies.values():
                enemy.rect.move_ip(-globalvars.GLOBAL_DELTA_X, -globalvars.GLOBAL_DELTA_Y)
                if enemy.rect.x > 1224 or enemy.rect.x < -200 or enemy.rect.y > 968 or enemy.rect.y < -200:
                    deadenemies.append(enemy)
            for enemy in deadenemies:
                if enemy in self.world.enemies:
                    self.world.enemies.remove(enemy)
                    self.graphics.remove_enemy_shape(enemy)
            
        #Update Countdown Timer
        self.timer.Milli -= delta
        self.timer.update()
        
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
                                    pygame.mixer.Sound(self.slurp).play()
                                    enemy.randirx = 0
                                    enemy.randiry = 0
                            else:
                                player_piece = self.player.kill_shape(player_piece)
                                self.world.add_enemy_shape(player_piece)
                                pygame.mixer.Sound(self.crash).play()
                                self.player.set_invis(True)
                                return
                            break #do one collision per shape a frame

        
        
        
      
    
    