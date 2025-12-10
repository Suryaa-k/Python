# Q1. Create a class Student that:
# •	Keeps track of the total number of students created.
# •	Determines whether a student passed or failed based on a shared passing mark.
# •	Provides a method to curve marks by increasing everyone’s marks by a percentage.
# •	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).

class Student:
    total_students = 0
    passing_marks = 40
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.total_students += 1
        if self.passing_marks>marks:
            Student.passing_marks = marks
    @classmethod
    def update_marks(cls,new_marks):
        cls.passing_marks += new_marks
        cls.new_marks = 40
    @staticmethod
    def result(marks):
        if marks > 40:
            return "Passed"
        else:
            return "Failed"
    @staticmethod
    def grades(marks):
        if marks>100:
            return "Invalid Marks"
        elif (marks<100) and (marks>=75):
            return "A"
        elif (marks<75) and (marks>=60):
            return "B"
        elif (marks<60) and (marks>=40):
            return "C"
        else:
            return "F"

obj1=Student(input("Enter Name: "),int(input("Enter Marks: ")))
print(f"{obj1.name} is {obj1.result(obj1.marks)} & {obj1.grades(obj1.marks)} Grade ")
obj2=Student(input("Enter Name: "),int(input("Enter Marks: ")))
print(f"{obj2.name} is {obj2.result(obj2.marks)} & {obj2.grades(obj2.marks)} Grade ")
obj3=Student(input("Enter Name: "),int(input("Enter Marks: ")))
print(f"{obj3.name} is {obj3.result(obj3.marks)} & {obj3.grades(obj3.marks)} Grade ")
print(Student.passing_marks)

