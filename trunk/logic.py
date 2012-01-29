import pygame

class Logic:
    def __init__(self, player, scoreboard, timer, control):
        self.player = player
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
            
        #Update Countdown Timer
        self.timer.Milli -= delta
        self.timer.update()        

        #Update score value
        self.scoreboard.update()
        
      
    
    