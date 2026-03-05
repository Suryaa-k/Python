# 23 Write a program to find the largest element in a list.

l=list(map(int,input().split()))
max= -(10**6)

for i in l:
    if i>max:
        max=i
print(f"Max Number is: {max}")
