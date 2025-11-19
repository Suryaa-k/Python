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
def calling(obj):
       print(obj.geta())
obj1=A(20)
obj2=B(10,30)
calling(obj1)
calling(obj2)



