# 5 Write a program to remove an element from a list using its index.

l=list(map(int,input().split()))
index=int(input())
l.remove(l[index])
print(l)