from shape import Shape

class Square(Shape):
    
    shape_type = "square"

    def __init__(self, size, rotation, color="blue"):
        texture_path = Shape.build_texture_path(color, shape_type)
        Shape.__init__(self, texture_path, size, rotation)
    