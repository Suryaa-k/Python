# 6. Create a class in a module that uses private attributes and @property / 
# @setter decorators. Import the class into another module and show how 
# encapsulation protects the data while still allowing controlled access.

import random
class Demo:
    def __init__(self, name):
        self.name = name
        self.__id = random.randint(1, 1000)

    @property
    def roll_num(self):
        return self.__id
    @roll_num.setter
    def roll_num(self, roll_num):
        x = input("Enter the pin : ")
        if x == "123456":
            self.__id = roll_num

    def display(self):
        print(f"Name : {self.name}\nRoll Number : {self.roll_num}")