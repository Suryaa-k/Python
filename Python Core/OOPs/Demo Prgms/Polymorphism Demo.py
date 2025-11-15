#Polymorphism

#Method Overriding
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

#Operator Overloading:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(f"({p3.x}, {p3.y})")  # Output: (4, 6)

#Duck Typing:
class Car:
    def move(self):
        return "Driving"
class Boat:
    def move(self):
        return "Sailing"
def transport(vehicle):
    return vehicle.move()
car = Car()
boat = Boat()
print(transport(car))  # Output: Driving
print(transport(boat))  # Output: Sailing