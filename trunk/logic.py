import pygame

class Logic:
    def __init__(self, player, scoreboard, timer, control):
        self.player = player
        self.scoreboard = scoreboard
        self.timer = timer
        self.control = control
    
    def update(self, delta):
        #Handle Input
        if self.control.rotateLeft:
            self.player.head.rotation = (self.player.head.rotation + 5) %360
        if self.control.rotateRight:
            self.player.head.rotation = (self.player.head.rotation - 5) %360
        if self.control.moveUp:
            if (self.player.head.rotation - 5) %360 <= 45 or (self.player.head.rotation - 5) %360 > 315:
                self.player.head.rect.move_ip(self.control.moverate, 0)
            if (self.player.head.rotation - 5) %360 <= 135 and (self.player.head.rotation - 5) %360 > 45:
                self.player.head.rect.move_ip(0, -self.control.moverate)
            if (self.player.head.rotation - 5) %360 <= 225 and (self.player.head.rotation - 5) %360 > 135:
                self.player.head.rect.move_ip(-self.control.moverate, 0)
            if (self.player.head.rotation - 5) %360 <= 315 and (self.player.head.rotation - 5) %360 > 225:
                self.player.head.rect.move_ip(0, self.control.moverate)
                
        #Update Countdown Timer
        self.timer.Milli -= delta
        self.timer.update()        

        #Update score value
        self.scoreboard.update()
            
        
    