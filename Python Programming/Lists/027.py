# 27 Write a program to find the Nth largest element in a list.

numbers = [12, 45, 23, 67, 34, 89]
n = int(input("Enter the value of N: "))

numbers.sort(reverse=True)

if n <= len(numbers):
    print("Nth largest element is:", numbers[n-1])
else:
    print("N is larger than the list size")