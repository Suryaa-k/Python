
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute using name mangling

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary cannot be negative.")

# Create an Employee object
emp = Employee("Alice", 50000)

# Access public attribute
print(f"Employee Name: {emp.name}")

# Access private attribute using a getter method
print(f"Employee Salary: {emp.get_salary()}")

# Modify private attribute using a setter method
emp.set_salary(60000)
print(f"Updated Salary: {emp.get_salary()}")
