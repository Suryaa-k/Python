#Isomorphic

s=input()
t=input()
d={}
if len(s)==len(t):
    for i in range(0,len(s)):
        if s[i] in d:
            if d[s[i]]!=t[i]:
                print("Not a Isomorphic")
                break
        else:
            if t[i] in d.values():
                print("Not a Isomorphic")
                break
            d[s[i]]=t[i]
    else:
        print("Isomorphic")
else:
    print("Not a Isomorphic")
