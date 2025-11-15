# Q2. Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.

class Employee:
    company_name="TechCorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_comapny(cls,new_name):
        cls.company_name=new_name
Emp1=Employee("Surya")
Emp2=Employee("Anish")
print(Emp1.company_name)
print(Emp2.company_name)
Emp1.change_comapny("CVCorp")
print(Emp1.company_name)
print(Emp2.company_name)








