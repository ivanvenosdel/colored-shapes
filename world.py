from actors import *
from ui import Scoreboard

class World:
    def __init__(self, player):
        self.enemies = {}
        self.player = player
        self.numenemy = 0
        self.i = 0
        
    def update(self, delta):
        pass
        
    def create_shape(self, shape_type, size, rotation, color):
        if shape_type == "hexagon":
            return Hexagon(size, rotation, color)
        elif shape_type == "octagon":
            return Octagon(size, rotation, color)
        elif shape_type == "pentagon":
            return Pentagon(size, rotation, color)
        elif shape_type == "shape":
            return Shape(size, rotation, color)
        else: #tri
            return Tri(size, rotation, color)
            
    def add_enemy(self, shape_type, color, size, rotation):
        shape = self.create_shape(shape_type, size, rotation, color)
        self.enemies[shape.id] = shape
        self.numenemy += 1
        
    def remove_enemy(self, shapeid):
        if shapeid in self.enemies:
            del self.enemies[shapeid]
        
    def eat_enemy(self):
        while self.i < self.numenemy:
            self.ate = pygame.sprite.collide_rect(self.player, self.enemies[self.i])
            if self.ate:
                pass
            self.i += 1