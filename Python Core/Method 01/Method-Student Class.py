# Q10. Create a class Student with:
# •	class variable passing_marks = 40
# •	instance attributes name, marks
# •	instance method result() → prints pass/fail using class variable
# •	class method update_passing_marks(cls, new_marks)
# •	static method grade_category(marks) → returns "A", "B", "C" based on score ranges

class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if (Student.passing_marks >=40):
            return "Pass"
        else:
            return "Fail"
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks >= 75:
            return "A"
        elif marks >= 50:
            return "B"
        elif marks >= 35:
            return "C"
        else:
            return "Fail"
name = input("Enter your name: ")
marks = int(input("Enter the marks: "))
student_obj = Student(name, marks)
print("Status:", student_obj.result())
print("Grade:", Student.grade_category(student_obj.marks))



