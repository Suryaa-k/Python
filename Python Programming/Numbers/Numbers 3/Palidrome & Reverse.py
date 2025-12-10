n = int(input())
c = 0
t = n
s = 0
if n == 0:
    print("Zero")
elif n < 0:
    print("Invalid Input")
else:
    while t > 0:
        r = t % 10
        s = s * 10 + r
        t = t // 10
    if n == s:
        print("Given Number is Palindrome")
    else:
        print(f"Reverse of a Given Number is {s}")
