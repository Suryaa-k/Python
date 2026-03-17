# 41 Write a program to rotate a list by k positions.

l = list(map(int, input().split()))
k = int(input())
a = l[0 : k]
for i in range(len(a)):
    t = l.pop()
    l.insert(0, t)
print(l)