# 40 Write a program to print all rotations of a list (anticlockwise)

l = list(map(int, input().split()))
for i in range(len(l)):
    t = l.pop()
    l.insert(0, t)
    # print(l)

# or

for i in range(len(l)):
    t = l[len(l)-1]
    for j in range(len(l)-1, -1, -1):
        l[j] = l[j-1]
    l[0] = t
    print(l)