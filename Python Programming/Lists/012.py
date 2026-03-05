# 12 Write a program to calculate the average of prime numbers in a list.

l=list(map(int,input().split()))
sum=0
c=0
for i in range(len(l)):
    sum+=l[i]
    c+=1
avg=sum/c
print("%.2f"%avg)