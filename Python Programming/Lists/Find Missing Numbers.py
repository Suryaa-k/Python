# 29 Write a program to find missing numbers in a sorted list.

numbers = [1, 2, 4, 6, 7, 10]

print("Missing numbers are:")

for i in range(len(numbers) - 1):
    for num in range(numbers[i] + 1, numbers[i + 1]):
        print(num)