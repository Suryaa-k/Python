from .base import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def description(self):
        return f"Circle(r={self.radius})"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def description(self):
        return f"Rectangle({self.width}x{self.height})"
