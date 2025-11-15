
class ParentClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name} from the parent class.")

class ChildClass(ParentClass):  # ChildClass inherits from ParentClass
    def __init__(self, name, age):
        super().__init__(name)  # Calls the parent class's __init__ method
        self.age = age

    def introduce(self):
        print(f"I am {self.name}, and I am {self.age} years old.")

# Create instances
parent_obj = ParentClass("Surya")
child_obj = ChildClass("Adithyaa", 30)

parent_obj.greet()
child_obj.greet()  # Child inherits the greet method so gets parent Class
child_obj.introduce()