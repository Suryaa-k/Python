# 1 Write a program to create a list by taking input from the user and print the list.

lis=list(map(int,input("Enter List: ").split()))
for i in lis:
    print(i,end=" ")