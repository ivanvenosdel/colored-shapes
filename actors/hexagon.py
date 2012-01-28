from shape import Shape

class Hexagon(Shape):

    def __init__(self, color="blue"):
        Shape.__init__(self, "hex", color)
    