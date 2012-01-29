import random
import uuid

from actors.shape import Shape

class Head(Shape):
    
    def __init__(self, size, rotation):
        Shape.__init__(self, "head.png", size, rotation)
        
        self.sides = 1
        
    