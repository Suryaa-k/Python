class Animal:
    def new_sound(self):
        print("sound")
class Dog(Animal):
    def make_sound(self):
        print("Bow")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
class Cow(Animal):
    def make_sound(self):
        print("Ambaa")
obj1=Dog()
obj2=Cat()
obj3=Cow()
obj1.make_sound()
obj2.make_sound()
obj3.make_sound()
