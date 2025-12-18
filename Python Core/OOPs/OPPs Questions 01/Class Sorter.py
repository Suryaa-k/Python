# Q7. Create:
# • Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS,
# each implementing a different logic method.
# Demonstrate how polymorphism can be achieved without inheritance by using
# interchangeable strategy objects.

class Sorter:
    def change(self, Strategy):
        Strategy.logic()

class BS:
    def logic(self):
        print("Binary Sorting")

class MS:
    def logic(self):
        print("Merging Sorting")

class QS:
    def logic(self):
        print("Quick Sorting")

obj = BS()
obj1 = MS()
obj2 = QS()
li = [obj,obj1,obj2]
s = Sorter()
for i in li:
    s.change(i)