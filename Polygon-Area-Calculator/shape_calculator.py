class Rectangle():

    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)


    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


    def set_width(self, width):
        self.width = width


    def set_height(self, height):
        self.height = height


    def get_area(self):
        return self.width * self.height


    def get_perimeter(self):
        return 2 * (self.width + self.height)


    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5


    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for _ in range(self.height):
                picture += "*" * self.width + '\n'
        return picture


    def get_amount_inside(self, shape):
        columns = int(self.width / shape.width)
        rows = int(self.height / shape.height)

        return columns * rows


class Square(Rectangle):

    def __init__(self, side):
        self.set_side(side)


    def __str__(self):
        return f"Square(side={self.width})"


    def set_side(self, side):
        self.width = side
        self.height = side


    def set_width(self, width):
        self.set_side(width)


    def set_height(self, height):
        self.set_side(height)
