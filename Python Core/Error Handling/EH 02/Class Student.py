# Create a class Student with an attribute marks. Implement a method 
# set_marks(marks) that raises a ValueError if marks are not in the range 0 to 100.

class Student:
    def __init__(self):
        self.marks=0
    def set_marks(self,m):
        if m<0 or m>100:
            raise ValueError("Msg")
        self.marks=m
        