class A:
    def m1(self,age):
        if age<18:
            raise ValueError("Age is less than or equal to 18")

a=A()

try:
    age = int(input("Enter age: "))
    a.m1(age)
except ValueError as v:
    print(v)

# Define the Error
# Define Error
# Try (Test) the error
# Except (Rename the Error)
# Get Output

