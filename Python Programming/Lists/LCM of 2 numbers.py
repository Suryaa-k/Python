# 20 Write a program to find the LCM of two numbers.

l=list(map(int,input().split()))
v1=int(input())
v2=int(input())
h=max(v1,v2)
m=h
if v1 and v2 in l:
    while True:
            if h%v1==0 and h%v2==0:
                print(h)
                break
            h+=m