# Q4. Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.

class Car:
    milage=30
    def __init__(self):
        self.wheels=4
    def display_specs(self):
        print(self.milage)
        print(self.wheels)
    def change_wheels(self,new_wheels):
        self.wheels=new_wheels
obj=Car()
obj.display_specs()
obj.change_wheels(new_wheels=6)
obj.display_specs()


