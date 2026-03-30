s="Qwert2345"
print(s.upper())

for i in range(len(s)):
    asi=ord(s[i])
    if asi>=97 and asi<=122:
        print(chr(asi-32),end="")
    else:
        print(chr(asi),end="")
