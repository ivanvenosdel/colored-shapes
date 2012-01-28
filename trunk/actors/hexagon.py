from shape import Shape

class Hexagon(Shape):

    def __init__(self, color="blue"):
        self.color = color
        if color == "blue":
            self.texture_path = 'blue_hex.png'
        elif color == "red":
            self.texture_path = 'red_hex.png'
        elif color == "green":
            self.texture_path = "green_hex.png"
        self.image, self.rect = imageutils.load_image(self.color, -1)
    