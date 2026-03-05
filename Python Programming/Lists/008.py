# 8 Write a program to print the list in reverse order.

l=list(map(int,input().split()))
l1=[ ]
for i in range(len(l)):
    l1.insert(0,l[i])
print(l1)