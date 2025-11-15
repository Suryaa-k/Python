def ispal(i):
    rev,t=0,i
    while t>0:
        r=t%10
        rev=rev*10+r
        t=t//10
    return i==rev
n=int(input())
m=int(input())
c=0
s=0
if n<0 or m<0:
    print("Invalid Inputs")
else:
    for i in range(n,m+1):
        if ispal(i):
            s+=1
            if s%2==1:
                c=c+1
                if c!=1:
                    print(", ",end="")
                print(i,end="")
    if c==0:
        print("No Palindromes")
    else:
        print(", ",end="")