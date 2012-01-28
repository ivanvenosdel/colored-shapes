from shape import Shape

class Tri(Shape):

    def __init__(self, color="blue"):
        Shape.__init__(self, "tri", color)
    