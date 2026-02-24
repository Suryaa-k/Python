# Binary Search Algorithm

l=list(map(int,input().split()))
key=int(input())
l.sort()
s=0, e=len(l)-1
while s<e:
    mid=(s+e)//2
    if l[mid]==key:
        print("Element found at index",mid)
        break
    elif l[mid]>key:
        e=mid-1
    else:
        s=mid+1