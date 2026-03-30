s="Qwert2345"
print(s.lower())

for i in range(len(s)):
    asi=ord(s[i])
    if asi>=65 and asi<=91:
        print(chr(asi+32),end="")
    else:
        print(chr(asi),end="")