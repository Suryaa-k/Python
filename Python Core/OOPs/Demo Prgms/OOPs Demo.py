#  Create a base class Transport with move() and derived classes Bus
#  and Bike, which have the same "move" method but with different behaviour
#  it but also call the parent implementation using super().

class Transport:
    def move(self):
        print("Moving")
class Bike(Transport):
    def move(self):
        print("Bike")
        super().move()
class Bus(Transport):
    def move(self):
        print("Bus")
        super().move()
bike1=Bike()
bus1=Bus()
bike1.move()
bus1.move()


class A:
    def m1(self):
        print("m1 in A")
class B(A):
    def m1(self):
        print("m1 in B")
        super().m1()
obj=A()
obj.m1()
obj1=B()
obj1.m1()



class X:
    def m1(self):
        print("m1 in X")
class Y:
    def m1(self):
        print("m1 in Y")
class Z:
    pass
def calling_m1(x):
    x.m1()
obj=X()
obj1=Y()
obj2=Z()
calling_m1(obj)
calling_m1(obj1)


class Dog:
    def quack(self):
        print("Dog")
class Duck:
    def quack(self):
        print("Duck")
def make_it_speak(x):
    x.quack()
dogesh=Dog()
quackesh=Duck()
make_it_speak(dogesh)
make_it_speak(quackesh)