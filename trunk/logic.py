import pygame

class Logic:
    def __init__(self, player, scoreboard, timer, control):
        self.player = player
        self.scoreboard = scoreboard
        self.timer = timer
        self.control = control
    
    def update(self, delta):
        #Handle Input
        if self.control.moveLeft:
            self.player.head.rect.move_ip(-self.control.moverate, 0)
        if self.control.moveRight:
            self.player.head.rect.move_ip(self.control.moverate, 0)
        if self.control.moveUp:
            self.player.head.rect.move_ip(0, -self.control.moverate)
        if self.control.moveDown:
            self.player.head.rect.move_ip(0, self.control.moverate)       
       
        #Update Countdown Timer
        self.timer.Milli -= delta
        self.timer.update()        

        #Update score value
        self.scoreboard.update()
            
        
    