class Employee:
    company_name="XYZ"
    increment=0.2
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def withstring(cls,s):
        name,salary=s.split("-")
        return cls(name,int(salary))
    @classmethod
    def getcomp(cls):
        return cls.company_name
    def update_salary(self):
        self.salary=self.salary+(self.salary*self.increment)
    @staticmethod
    def m1(salary):
        if salary>40000:
            print("Rich Guy")
        else:
            print("Poor Guy")
obj=Employee("John",20000)
obj1=Employee.withstring("Anurag-50000")
obj.update_salary()
print(obj.salary)
obj1.m1(obj1.salary)
