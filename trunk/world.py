from actors import *

class World:
    def __init__(self):
        self.enemies = {}
    
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
        
    def remove_enemy(self, shapeid):
        if shapeid in self.enemies:
            del self.enemies[shapeid]
        
    