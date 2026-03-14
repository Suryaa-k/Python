# 15 Write a program to print the next prime number for each element in the list.

l=list(map(int,input().split()))
for i in range(len(l)):
    n=l[i]+1
    while True:
        fc=0
        for j in range(1,n+1):
            if n%j==0:
                fc+=1
        if fc==2:
            print(n)
            break
        n+=1
print(l)