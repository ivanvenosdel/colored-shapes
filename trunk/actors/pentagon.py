from shape import Shape

class Pentagon(Shape):

    def __init__(self, size, rotation, color="blue"):
        Shape.__init__(self, "pentagon", color, size, rotation)
    