# You are building an employee payroll system.

class Employee:

    def __init__(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary

    def show_salary(self):
        print(f"{self.name}'s Salary: {self.__salary}")

class Manager(Employee):

    def __init__(self, name, department, salary, bonus):
        super().__init__(name, department, salary)
        self.__salary = salary + bonus

    def show_manager_salary(self):
        print(f"Manager {self.name}'s total salary (with bonus): {self.__salary}")

    def show_department(self):
        # Accessing protected attribute
        print(f"{self.name} manages the {self._department} department")

emp = Employee("Anish", "IT", 50000)
mgr = Manager("Surya", "Finance", 80000, 20000)

print(emp.name)
print(emp._department)
print(emp.__salary)
print(emp._Employee__salary)
mgr.show_manager_salary()
mgr.show_department()

mgr.show_salary()