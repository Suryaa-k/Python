# --- Input matrix A ---
r1 = int(input("Enter rows of A: "))
c1 = int(input("Enter cols of A: "))

print("Enter elements of A:")
a = []
for i in range(r1):
    row = list(map(int, input(f"  Row {i+1}: ").split()))
    a.append(row)

# --- Input matrix B ---
r2 = int(input("Enter rows of B: "))
c2 = int(input("Enter cols of B: "))

if c1 != r2:
    print("Multiplication not possible: cols of A must equal rows of B")
else:
    print("Enter elements of B:")
    b = []
    for i in range(r2):
        row = list(map(int, input(f"  Row {i+1}: ").split()))
        b.append(row)

    # --- Multiply ---
    res = []
    for i in range(0, r1):
        row = []
        for j in range(0, c2):
            total = 0
            for k in range(0, c1):
                total += a[i][k] * b[k][j]
            row.append(total)
        res.append(row)

    print("\nResult:")
    for row in res:
        print(row)