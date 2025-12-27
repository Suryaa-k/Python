from shapes.figures import Circle, Rectangle
from shapes.base import Shape

# Polymorphic list of shapes
shapes: list[Shape] = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3),
    Rectangle(2, 8)
]

print("Polymorphism Demo:")
for shape in shapes:
    print(shape.display())  # Calls overridden methods dynamically

# Type checking works too
print("\nType checks:")
print(isinstance(shapes[0], Shape))  # True
