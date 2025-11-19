#Try to Implement polymorphism, Inheritance, Encapsulation in a Single Program

class A:
    def __init__ (self,a):
        self.__a=a 
    def geta(self):
        return self.__a
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.__b=b 
    def geta(self):
        print(super().geta())
        return self.__b 
obj=B(10,20)
print(obj.geta()) #Printing both a&b values
obj1=A(30)
print(obj1.geta()) # Printing only A value 



