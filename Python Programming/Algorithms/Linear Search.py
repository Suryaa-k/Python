# Linear Search Algorithm (Method 1)

l=list(map(int,input().split()))
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i]==l[j]:
            c+=1
    print(l[i],c)

# Linear Search Algorithm (Method 2)
l=list(map(int,input().split()))
for i in range(len(l)):
    c=l.count(l[i])
    print(l[i],c) 