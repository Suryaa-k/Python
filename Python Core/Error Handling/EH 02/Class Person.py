# • Create a class Person whose constructor takes age as an argument. Raise a 
# ValueError if the age is less than 0.

class Person:
    def __init__(self,age):
        if age<0:
            raise ValueError("Message")
        self.age=age 
try:
    obj=Person(18)
    obj2=Person(-5)
except ValueError as e:
    print(e)