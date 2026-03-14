# 10 Write a program to calculate the sum of list elements up to a given index.

l=list(map(int,input().split()))
index=int(input())
sum=0
for i in range(len(l)):
    if i<=index:
        sum+=l[i]
print(sum)