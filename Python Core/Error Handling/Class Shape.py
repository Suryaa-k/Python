#  Create a base class Shape with a method area() that raises 
# NotImplementedError. Create a child class Rectangle that overrides and 
# implements the area method.

class Shape:
    def area(self):
        
        raise NotImplementedError("Subclasses must implement the area() method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(5, 3)
print("Area of rectangle:", r.area())  
