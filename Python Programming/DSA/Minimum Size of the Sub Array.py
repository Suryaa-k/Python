#Minimum Size of the Sub Array
#Dynamic Sliding Window

l=[2, 3, 1, 4, 3, 5, 8, 2, 11]
tar=10
su=0
milen=10**6
miar=[]
for j in range(len(l)):
    for i in range(j,len(l)):
        su+=l[i]
        if su>=tar:
            milen=j-i+1
            miar=l[j:i+1]
            su=0
            break
print(milen)
print(miar)
