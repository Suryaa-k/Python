# Unsorted / With Duplicates

def twosum(l,tar):
    s=set()
    for i in l:
        ch=tar-i
        print(i)
        if ch in s:
            print(i,tar-i)
            return [i,tar-i]
        s.add(i)
l=[10,7,18,2,4,6,25]
tar=20
print(twosum(l,tar))



