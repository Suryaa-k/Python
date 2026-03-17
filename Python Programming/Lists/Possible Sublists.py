# 42 Write a program to print all possible sublists of a list.

l = list(map(int, input().split()))
for i in range(len(l)):
    for j in range(i, len(l)):
        for k in range(i, j+1):
            print(l[k], end = " ")
        print()

# or

for i in range(len(l)):
    a = []
    for j in range(i, len(l)):
        a.append(l[j])
        print(a)
