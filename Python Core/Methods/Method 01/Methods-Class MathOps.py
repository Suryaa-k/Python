# Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
# Then call it both from the class and an instance.

class MathOps:
    def __init__(self,num):
        self.num=num
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return True
        return False

print(MathOps.is_even(5))
Obj1=MathOps(10)
print(Obj1.is_even(Obj1.num))
