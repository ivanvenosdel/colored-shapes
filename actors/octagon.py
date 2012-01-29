from shape import Shape

class Octagon(Shape):
    
    shape_type = "octagon"

    def __init__(self, size, rotation, color="blue"):
        texture_path = Shape.build_texture_path(color, Octagon.shape_type)
        Shape.__init__(self, texture_path, size, rotation, Octagon.shape_type)
    
        self.sides = 8
        self.color = color
        