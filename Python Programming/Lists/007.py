# 7 Write a program to count the number of occurrences of an element in a list.

l=list(map(int,input().split()))
value=int(input())
c=0
for i in range (len(l)):
    if l[i]==value:
        c+=1
print(f"{value}-{c}")