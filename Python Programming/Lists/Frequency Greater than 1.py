# 38 Write a program to print elements whose frequency is greater than 1.

l = list(map(int, input().split()))
for i in range(len(l)):
    c, d = 0, 0
    for j in range(len(l)):
        if l[i] == l[j]:
            c+=1
    for j in range(0, i+1):
        if l[i]==l[j]:
            d+=1
    if c>1:
        if d==1:
            print(l[i])