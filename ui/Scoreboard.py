import pygame

class Scoreboard:
    def __init__(self):
        self.font = pygame.font.SysFont('tahoma', 30)
        self.font.set_italic(1)
        self.color = pygame.Color('white')
        self.lastscore = -1
        self.currentscore = 0
        self.update()
        self.rect = self.image.get_rect().move(0, 450)
        
        
    def update(self):
        if self.currentscore != self.lastscore:
            self.lastscore = self.currentscore
            msg = "Score: %d" % self.currentscore
            self.image = self.font.render(msg, 0, self.color)
