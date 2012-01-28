from shape import Shape

class Square(Shape):

    def __init__(self, size, rotation, color="blue"):
        Shape.__init__(self, "square", color, size, rotation)
    