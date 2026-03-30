s="Surya Anish K"
print(s.replace(" ","-"))
result = ""
i = 0
while i < 1000:
    try:
        char = s[i]
        if char == " ":
            result += "-"
        else:
            result += char
        i += 1
    except:
        break
print(result)



