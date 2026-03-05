# 19 Write a program to check whether a list is sorted or not.

l=list(map(int,input().split()))
k=False
for i in range (len(l)-1):
    if l[i]<l[i+1] or l[i]==l[i+1]:
        k=True
    else:
        k=False
        break
if k == True:
    print("list is sorted")
else:
    print("list is not sorted")