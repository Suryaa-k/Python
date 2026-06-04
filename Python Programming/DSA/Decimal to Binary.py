def decimal_to_binary(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(n % 2)
        n = n // 2
    return ''.join(str(b) for b in reversed(bits))

num = int(input("Enter a decimal number: "))
result = decimal_to_binary(num)
print(f"Binary: {result}")