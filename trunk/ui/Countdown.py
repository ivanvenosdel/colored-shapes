import pygame

class CountDown:
    def __init__(self):
        self.font = pygame.font.SysFont('stencil', 40)
        self.color = pygame.Color('White')
        self.lowcolor = pygame.Color('Red')
        self.Minutes = 0
        self.Seconds = 10
        self.Milli = 60
        self.update()
        self.rect = self.image.get_rect().move(0, 450)
        
    def update(self):
        if(self.Seconds <= 0 and self.Minutes <= 0):
            self.Seconds = 0
            self.Minutes = 0
        elif(self.Seconds <= 0):
            self.Seconds = 60
            self.Minutes -= 1
        elif(self.Milli <= 0):
            self.Milli = 1000
            self.Seconds -= 1
        elif(self.Seconds > 60):
            self.Seconds = self.Seconds - 60
            self.Minutes += 1
        elif(self.Milli > 1000):
            self.Milli = self.Milli - 1000
            self.Seconds += 1
        if(self.Minutes >= 10):
            if(self.Seconds >= 10):
                msg = "%d:%d" % (self.Minutes, self.Seconds)
                self.image = self.font.render(msg, 0, self.color)
            if(self.Seconds < 10):
                msg = "%d:0%d" % (self.Minutes, self.Seconds)
                self.image = self.font.render(msg, 0, self.color)
        if(self.Minutes < 10):
            if(self.Seconds >= 10):
                msg = "0%d:%d" % (self.Minutes, self.Seconds)
                self.image = self.font.render(msg, 0, self.color)
            if(self.Seconds < 10):
                msg = "0%d:0%d" % (self.Minutes, self.Seconds)
                self.image = self.font.render(msg, 0, self.color)        
        if(self.Minutes == 0 and self.Seconds <= 10):
            self.image = self.font.render(msg, 0, self.lowcolor)