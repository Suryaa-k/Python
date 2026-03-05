# 13 Write a program to calculate the average of odd numbers in a list.

l=list(map(int,input().split()))
sum=0
c=0
for i in range(len(l)):
    if l[i]%2==1:
        sum+=l[i]
        c+=1
avg=sum/c
print("%.2f"%avg)
