# [1 -2 -10 5]

l = [1, 2, -3, -4, 5, 7]
lp = []
ln = []
op = []

for i in l:
    if i > 0:
        lp.append(i)
    else:
        ln.append(i)

if len(lp)>len(ln):
    le=len(lp)
else:
    le=len(ln)

print(le)
for i in range(0,le):
    if i<len(lp) :
        print(lp[i],end=" ")
    if i<len(ln):
        print(ln[i],end=" ")

