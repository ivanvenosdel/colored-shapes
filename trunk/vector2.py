import math

class Vector2:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "x: %s, y: %s" % (self.x, self.y)

    @classmethod
    def from_points(cls, point1, point2):
        return cls( point2[0] - point1[0], point2[1] - point1[1])
    
    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )
    
    def normalize(self):
        magnitude = self.get_magnitude()
        normal_x = self.x / magnitude
        normal_y = self.y / magnitude
        return (normal_x, normal_y)
    