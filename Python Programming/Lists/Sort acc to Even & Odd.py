# 30 Write a program to sort a list such that all even numbers come first, followed by odd numbers.

# Input list
my_list = list(map(int,input().split()))

i = 0
length = 0
while i < 100:
    try:
        temp = my_list[i]
        length += 1
    except:
        break
    i += 1

even_pos = 0
odd_pos = 0
result = [0] * length

i = 0

while i < length:
    num = my_list[i]
    if num % 2 == 0:  # Even
        result[even_pos] = num
        even_pos += 1
    i += 1

i = 0
while i < length:
    num = my_list[i]
    if num % 2 != 0:  # Odd
        result[odd_pos + even_pos] = num  # After evens
        odd_pos += 1
    i += 1

print("Input:", my_list[:length])
print("Output:", result)