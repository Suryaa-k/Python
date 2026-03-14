# 25 Write a program to find the third largest element in a list.

l=list(map(int,input().split()))
max1= -(10**6)
max2= -(10**6)
max3= -(10**6)

for i in l:
    if i>max1:
        max3=max2
        max2=max1
        max1=i

    elif i>max2 and i!=max1:
        max3=max2
        max2=i

    elif i>max3 and i!=max2 and i!=max1:
        max3=i

print(f"Max Number is: {max1}")
print(f"Second Max Number is: {max2}")
print(f"Third Max Number is: {max3}")