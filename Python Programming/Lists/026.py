# 26 Write a program to sort a list without using any built-in sorting functions.

l = list(map(int,input().split()))

n = len(l)

for i in range(n):
    for j in range(0, n - i - 1):
        if l[j] > l[j + 1]:
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp

print("Sorted list:", l)