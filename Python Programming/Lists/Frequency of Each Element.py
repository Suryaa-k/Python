# 31 Write a program to find the frequency of each element in a list.

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

visited = [0] * length
i = 0

while i < length:
    if visited[i] == 0:
        current = my_list[i]
        count = 0

        j = 0
        while j < length:
            if my_list[j] == current:
                count += 1
            j += 1

        print(f"{current}: {count}")

        j = 0
        while j < length:
            if my_list[j] == current:
                visited[j] = 1
            j += 1

    i += 1
