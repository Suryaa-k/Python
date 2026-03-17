# 36 Write a program to find the least unique element in a list.

l = list(map(int, input().split()))
ele = 10**6
for i in range(len(l)):
    c = 0
    for j in range(len(l)):
        if l[i]==l[j]:
            c+=1
    if c==1:
        if l[i]<ele:
            ele = l[i]
print(ele)