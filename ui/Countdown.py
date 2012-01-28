import pygame

class CountDown:
    def __init__(self):
        self.font = pygame.font.Font(None, 40)
        self.font.set_bold(1)
        self.color = pygame.Color('White')
        self.lowcolor = pygame.Color('Red')
        self.Minutes = 1
        self.Seconds = 10
        self.Milli = 60
        self.update()
        self.rect = self.image.get_rect().move(0, 450)
        
    def update(self):
        if(self.Seconds <= 0):
            self.Seconds = 60
            self.Minutes -= 1
        if(self.Milli <= 0):
            self.Milli = 1000
            self.Seconds -= 1
        if(self.Seconds > 60):
            self.Seconds = self.Seconds - 60
            self.Minutes += 1
        if(self.Milli > 1000):
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
        if(self.Minutes == 0):
            self.image = self.font.render(msg, 0, self.lowcolor)