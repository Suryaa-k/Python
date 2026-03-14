# 21 Write a program to find the GCD of two numbers.

l=list(map(int,input().split()))
n1=int(input())
n2=int(input())
m=min(n1,n2)
if n1 and n2 in l:
    for i in range(m,0,-1):
            if n1%i==0 and n2%i==0:
                print(i)
                break