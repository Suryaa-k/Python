#Create a class Employee with:
#instance attributes: name, base_salary
#class variable: bonus_rate = 0.1
#instance method: final_salary() → base_salary + (base_salary × bonus_rate)
#class method: update_bonus(cls, new_rate) → updates bonus for all employees
#static method: is_valid_salary(sal) → checks if salary > 0
#Create two employees, show final salaries, update bonus rate, and show again.

class Employee:
    bonus_rate=0.1
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def final_salary(self):
        return self.base_salary + (self.base_salary * Employee.bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.update_salary=new_rate
    @staticmethod
    def is_valid_salary(salary):
        return salary >= 0
Emp1 = Employee("Surya", 10000)
Emp2 = Employee("Anish", 20000)

Employee.update_bonus(0.2)
print(Emp1.final_salary())
print(Emp2.final_salary())

print(Employee.is_valid_salary(Emp1.base_salary))
print(Employee.is_valid_salary(-100))



