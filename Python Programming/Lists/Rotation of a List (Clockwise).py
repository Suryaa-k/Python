# 39 Write a program to print all rotations of a list (clockwise)

l = list(map(int, input().split()))
for i in range(len(l)):
    a = l.pop(0)
    l.append(a)
    # print(l)

#  or

for i in range(len(l)):
    t = l[0]
    for j in range(len(l)-1):
        l[j] = l[j+1]
    l[len(l)-1] = t
    print(l)