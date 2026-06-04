def binary_to_decimal(b):
    result = 0
    for i, bit in enumerate(reversed(b)):
        result += int(bit) * (2 ** i)   # digit × 2^position
    return result

num = input("Enter a binary number: ")
result = binary_to_decimal(num)
print(f"Decimal: {result}")
print(f"Verify using int(): {int(num, 2)}")

"or"

bin=int(input("Enter a binary number: "))
dec=0
p=len(bin)-1

for i in range(len(bin)):
    dec+= (int(bin[i])*(2 ** p))
    p-=1
print(f"Decimal: {dec}")