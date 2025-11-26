# 3.	Create: Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS, each implementing a different logic method.
# •	Demonstrate how polymorphism can be achieved without inheritance by using interchangeable strategy objects.

class Sorter:
    def change(self,strategy):
        strategy.logic()

class BS:
    def logic(self):
        print("BS")

class MS:
    def logic(self):
        print("MS")

class QS:
    def logic(self):
        print("QS")

S=Sorter()
obj,obj1,obj2=BS(),MS(),QS()

S.change(obj)
