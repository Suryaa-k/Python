# Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.

class Student(object):
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks >= 40:
            return True
        else:
            return False
    def result(self):
        if self.is_passed():
            print("Pass")
        else:
            print("Fail")
obj=Student(name="qwer",marks=23)
obj.result()
obj1=Student(name=input("Enter Name:"),marks=int(input("Enter Marks:")))






