# 2 Write a program to insert an element at a specific index in a list.

l=list(map(int,input("Enter List: ").split()))
index=int(input("Enter Index: "))
value=int(input("Enter Value: "))
l.insert(index,value)
print(l)