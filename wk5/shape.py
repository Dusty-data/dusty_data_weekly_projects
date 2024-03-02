class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def __init__(self,width, height):
        super().__init__(width, height)

    def calculate_area(self):
        return self.width * self.height
    

class Square(Shape):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def calculate_area(self):
        return self.width * self.height
    

# Create instances of Rectangle and Square
rectangle = Rectangle(4, 7)
square = Square(6)

# Calculate and print area of Rectangle
rectangle_area = rectangle.calculate_area()
print("Area of Rectangle:", rectangle_area)

# Calculate and print area of Square
square_area = square.calculate_area()
print("Area of Square:", square_area)