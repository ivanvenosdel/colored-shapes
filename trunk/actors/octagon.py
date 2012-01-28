from shape import Shape

class Octagon(Shape):

    def __init__(self, size, rotation, color="blue"):
        Shape.__init__(self, "octagon", color, size, rotation)
    