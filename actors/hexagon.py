from shape import Shape

class Hexagon(Shape):

    def __init__(self, size, rotation, color="blue"):
        Shape.__init__(self, "hex", color, size, rotation)
    