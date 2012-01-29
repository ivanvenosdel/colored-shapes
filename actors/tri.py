from shape import Shape

class Tri(Shape):
    
    shape_type = "tri"

    def __init__(self, size, rotation, color="blue"):
        texture_path = Shape.build_texture_path(color, Tri.shape_type)
        Shape.__init__(self, texture_path, size, rotation, Tri.shape_type, color)
        
        self.sides = 3
        self.color = color
    