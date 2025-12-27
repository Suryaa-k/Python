from Shapes.circle import Circle
from Shapes.rectangle import Rectangle

class ColoredCircle(Circle):  # Subclass from Circle
    def __init__(self, radius, color):
        super().__init__(radius)
        self.color = color
    
    def __str__(self):
        return f"ColoredCircle(radius={self.radius}, color='{self.color}')"

# Create parent class objects
parent_circle = Circle(5)
parent_rect = Rectangle(4, 6)

# Create child class object
child_circle = ColoredCircle(7, "red")

#Test them
print(parent_circle)        # Circle(radius=5)
print(f"Circle area: {parent_circle.area():.2f}")
print(parent_rect)          # Rectangle(4x6)
print(f"Rect area: {parent_rect.area()}") 
print(child_circle)         # ColoredCircle(radius=7, color='red')
print(f"Colored circle area: {child_circle.area():.2f}")

