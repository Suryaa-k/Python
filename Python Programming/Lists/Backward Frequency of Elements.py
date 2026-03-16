# 32 Write a program to calculate the backward frequency of elements in a list.

my_list = list(map(int, input().split()))

i = 0
length = 0
while i < 100:
    try:
        temp = my_list[i]
        length += 1
    except:
        break
    i += 1

i = length - 1
while i >= 0:
    current = my_list[i]
    count = 0
    j = length - 1

    while j >= 0:
        if my_list[j] == current:
            count += 1
        j -= 1

    print(f"{current}: {count}")
    i -= 1
