# 3. Use functools.reduce() with a lambda to find the largest number from a given list Dynamically.

from functools import reduce
li = [int(input("Enter Number: ")) for _ in range(int(input("Enter list size: ")))]
x = reduce(lambda x, y:x if x>y else y, li)
print(x)