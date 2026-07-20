n=int(input())
l=[-1]*(n+1)
l[1],l[2]=0,1
for i in range(3,n+1):
    l[i]=l[i-1]+l[i-2]
print(l[i],end=" ")