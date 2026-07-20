def maxsum(l,idx,dp):
    if dp[idx]!=-1:
        return dp[idx]
    if idx==0:
        return l[0]
    if idx==-1:
        return 0
    p=l[idx]+maxsum(l,idx-2,dp)
    np=maxsum(l,idx-1,dp)
    dp[idx]=max(p,np)
    return dp[idx]

l=(list(map(int,input().split())))
dp=[-1]*len(l)
maxsum(l,len(1)-1,dp)