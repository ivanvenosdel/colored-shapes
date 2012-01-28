from shape import Shape

class Square(Shape):

    def __init__(self, color="blue"):
        Shape.__init__(self, "square", color)
    