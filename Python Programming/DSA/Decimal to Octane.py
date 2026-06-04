def decimal_to_octal(n):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(n % 8)   # collect remainder (0–7)
        n = n // 8            # integer divide by 8
    return ''.join(str(d) for d in reversed(digits))

# Take input from user
num = int(input("Enter a decimal number: "))
result = decimal_to_octal(num)
print(f"Octal: {result}")
print(f"Verify using oct(): {oct(num)}")