# 34 Write a program to find the unique element in a list.

l = list(map(int, input().split()))
ele = 0
for i in range(len(l)):
    c = 0
    for j in range(len(l)):
        if l[i] == l[j]:
            c+=1
            ele = l[i]
    if c == 1:
        print(ele)