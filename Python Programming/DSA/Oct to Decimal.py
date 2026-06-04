def octal_to_decimal(o):
    result = 0
    for i, digit in enumerate(reversed(o)):
        result += int(digit) * (8 ** i)   # digit × 8^position
    return result

num = input("Enter an octal number: ")
result = octal_to_decimal(num)
print(f"Decimal: {result}")
print(f"Verify using int(): {int(num, 8)}")