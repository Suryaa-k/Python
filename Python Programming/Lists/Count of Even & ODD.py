# 14 Write a program to count the number of even and odd elements in a list.

l=list(map(int,input().split()))
ec=0   #even count
oc=0   #odd count
for i in range(len(l)):
    if l[i]%2==0:
        ec+=1
    else:
        oc+=1
print(ec)
print(oc)