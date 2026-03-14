# 3 Write a program to merge two lists into a single list.

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1.extend(l2)
print(l1)