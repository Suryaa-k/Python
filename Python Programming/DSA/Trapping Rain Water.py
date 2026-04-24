def fun(l):
    li = 0
    ri=len(l)-1
    lm=l[0]
    rm=l[-1]
    tw=0
    while li<ri:
        if l[li]<l[ri]:
            if l[li]>lm:
                lm=l[li]
            tw+=(lm-l[li])
            li+=1
        else:
            if l[ri]>rm:
                rm=l[ri]
            tw+=(rm-l[ri])
            ri-=1
    return tw

l=[1,2,0,1,3,5,0,9,7,3,7,4]
print(fun(l))


