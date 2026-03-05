# 6 Write a program to find the index of a given element in a list.

l=list(map(int,input().split()))
value=int(input())
for i in range (len(l)):
    if l[i]==value:
        print(i)