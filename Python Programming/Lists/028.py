# 28 Write a program to print the first four smallest elements from a list.

numbers = list(map(int,input().split()))

numbers.sort()

print("First four smallest elements are:")
for i in range(4):
    print(numbers[i])