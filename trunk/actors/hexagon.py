from shape import Shape

class Hexagon(Shape):
    
    shape_type = "hex"

    def __init__(self, size, rotation, color="blue"):
        texture_path = Shape.build_texture_path(color, Hexagon.shape_type)
        Shape.__init__(self, texture_path, size, rotation, Hexagon.shape_type)
        
        self.sides = 6
        self.color = color
    