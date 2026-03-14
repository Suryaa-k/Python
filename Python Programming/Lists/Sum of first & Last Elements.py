# 9 Write a program to find the sum of the first and last elements of a list.

l=list(map(int,input().split()))
print(l[0]+l[len(l)-1])