# 4 Write a program to remove a specific element from a list.

l=list(map(int,input().split()))
value=int(input())
l.remove(value)
print(l)