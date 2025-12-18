# Q4. Create a base class Transport with move() and derived classes Bus and Bike that
# override it but also call the parent implementation using super().
# Show the combination of reuse + custom behavior.

class Transport:
    def move(self):
        print("Moving Transport.")

class Bike(Transport):
    def move(self):
        super().move()
        print("Moving Bike.")

class Bus(Transport):
    def move(self):
        super().move()
        print("Moving Bus.")

obj = Bike()
obj.move()
obj1 = Bus()
obj1.move()