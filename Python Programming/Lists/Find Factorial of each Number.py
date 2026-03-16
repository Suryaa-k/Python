# 22 Write a program to find the factorial of each element in a list using recursion.

my_list = list(map(int, input().split()))

i = 0
length = 0
while True:
    if i >= 100:
        break
    try:
        temp = my_list[i]
        length += 1
    except:
        break
    i += 1

result = [0] * length
i = 0

while i < length:
    num = my_list[i]
    fact = 1
    j = 1

    while True:
        if j > num:
            break
        fact *= j
        j += 1
    result[i] = fact
    i += 1
print("Input:", my_list[:length])
print("Output:", result)