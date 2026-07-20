def nthgfib(n,l):
    if  l[n]!=-1:
        return l[n]
    if n<=2:
        return n-1
    l[n]=nthgfib(n-1,l)+nthgfib(n-2,l)
    return l[n]

n=int(input())
l=[-1]*(n+1)
print(nthgfib(n,l))