n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()
