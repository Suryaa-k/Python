# Q5. Create a class Course that:
# •	Tracks total courses created.
# •	Each course has a title, duration, and enrolled_students.
# •	Provides a method to enroll a new student.
# •	Allows updating the minimum duration for a valid course across all instances.
# •	Has a static function to check if a given duration is realistic (not negative, not too large).

class Course:
    total_students = 0
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.students = []

    def enroll(self,name):
        self.students.append(name)
        Course.total_students += 1
        print(f"{name} is enrolled")

    @classmethod
    def update_duration(cls, new_duration):
        cls.new_duration = new_duration

    @staticmethod
    def check_duration(hour, duration):
        if hour > duration or hour < 0:
            return False
        else:
            return True

obj1 = Course("Python", 45)
obj1.enroll(name="Surya")
print(obj1.students)
print(Course.total_students)
print(obj1.check_duration(30, obj1.duration))
print(obj1.check_duration(55, obj1.duration))

