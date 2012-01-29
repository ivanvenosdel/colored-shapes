from shape import Shape

class Pentagon(Shape):
    
    shape_type = "pentagon"

    def __init__(self, size, rotation, color="blue"):
        texture_path = Shape.build_texture_path(color, Pentagon.shape_type)
        Shape.__init__(self, texture_path, size, rotation, Pentagon.shape_type, color)
        
        self.sides = 5
        self.color = color
    