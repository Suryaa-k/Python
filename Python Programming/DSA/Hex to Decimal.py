def hex_to_decimal(h):
    hex_map = "0123456789ABCDEF"
    result = 0
    for i, ch in enumerate(reversed(h.upper())):
        result += hex_map.index(ch) * (16 ** i)  # digit × 16^position
    return result

num = input("Enter a hex number: ")
result = hex_to_decimal(num)
print(f"Decimal: {result}")
