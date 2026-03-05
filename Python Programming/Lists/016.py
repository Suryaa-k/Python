# 16 Write a program to perform linear search on a list.

def linear_search(l,value):
    for i in range(len(l)):
        if l[i] ==value:
            return i
    return -1
l=list(map(int,input().split()))
value=int(input())
result=linear_search(l,value)
if result != -1:
    print(f"Element {value} found at index {result}")
else:
    print(f"Element {value} not found")