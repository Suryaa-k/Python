n = int(input())
if n <= 0:
    print("Invalid Input")
else:
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()