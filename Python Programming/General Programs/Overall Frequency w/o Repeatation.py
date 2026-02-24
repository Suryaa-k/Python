l=list(map(int,input().split()))
for i in range(0,len(l)):
    oc=bc=0
    for j in range(0,len(l)):
        if (l[i]==l[j]):
            oc+=1
    for k in range(0,i+1):
        if (l[i]==l[k]):
            bc+=1
    if bc==1:
        print(l[i],oc)