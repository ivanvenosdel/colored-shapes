from shape import Shape

class Tri(Shape):

    def __init__(self, size, rotation, color="blue"):
        Shape.__init__(self, "tri", color, size, rotation)
    