# 11 Write a program to print all prime numbers present in a list.

l=list(map(int,input().split()))
for i in range(len(l)):
    fc=0
    for j in range(1,l[i]+1):
        if l[i]%j==0:
            fc+=1
    if fc==2:
        print(l[i])