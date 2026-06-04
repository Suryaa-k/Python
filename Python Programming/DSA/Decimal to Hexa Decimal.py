def decimal_to_hex(n):
    if n == 0:
        return "0"
    hex_digits = "0123456789ABCDEF"
    digits = []
    while n > 0:
        digits.append(hex_digits[n % 16])  # remainder 0–15 → char
        n = n // 16                       # integer divide by 16
    return ''.join(reversed(digits))

# Take input from user
num = int(input("Enter a decimal number: "))
result = decimal_to_hex(num)
print(f"Hexadecimal: {result}")
print(f"Verify using hex(): {hex(num).upper()}")