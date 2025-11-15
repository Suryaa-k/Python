n = int(input())
m = int(input())

def ispal(i):
    rev = 0
    t = i
    while t != 0:
        r = t % 10
        rev = rev * 10 + r
        t = t // 10
    return i == rev

if n < 0 or m < 0:
    print("Invalid Inputs")
else:
    if n > m:
        n, m = m, n
    c = 0
    for i in range(n, m + 1):
        if ispal(i):
            print(i)
            c += 1
    if c == 0:
        print("No Palindrome Values.")
