n, m = map(int, input().split())

if n <= 0 and m <= 0:
    print("Invalid Row and Column Values")
elif n <= 0:
    print("Invalid Row Value")
elif m <= 0:
    print("Invalid Column Value")
else:
    num = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            num += 1
            print(num, end=" ")
            if j != m:
                print("*", end=" ")
        print()
