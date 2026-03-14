# 18 Write a program to return all index positions of a searched element in a list.

l=list(map(int,input().split()))
value=int(input())
for i in range(len(l)):
    if l[i]==value:
        print(i,end=" ")