#Sorted List

def twosum(l,tar):
    s,e=0,len(l)-1
    while s<e:
        if l[s]+l[e]==tar:
            return [l[s],l[e]]
        elif l[s]+l[e]<tar:
            s+=1
        else:
            e-=1
    return -1

l=[2,4,6,7,10,18,25]
tar=13
print(twosum(l,tar))

