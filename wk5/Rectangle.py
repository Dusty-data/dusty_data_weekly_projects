# Creating a Python class called "Rectangle" that represents a rectangle. 
# The Rectangle class must have the following properties and methods: width (an integer) height (an integer)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area (self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
# Create an instance of the Rectangle class with width 5 and height 7
    
rectangle = Rectangle(5,7)

# printing area and perimeter

print("Area of the rectangle:", rectangle.area())
print("Perimeter of the rectangle:", rectangle.perimeter())
    

