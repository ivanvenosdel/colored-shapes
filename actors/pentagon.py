from shape import Shape

class Pentagon(Shape):

    def __init__(self, color="blue"):
        Shape.__init__(self, "pentagon", color)
    