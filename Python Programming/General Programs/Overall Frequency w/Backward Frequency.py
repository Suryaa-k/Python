#Backward Frequency

l=list(map(int,input().split())) 
for i in range(0,len(l)):
    c=0
    for j in range(0,len(l)):
        if l[i]==l[j]:
            c+=1
    print(l[i],c)
