def word_to_digit(s):
    d={"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    return d[s]
s=input().split()
for i in range(0,len(s)):
    if s[i]=="triple":
        print(word_to_digit(s[i+1]))
        print(word_to_digit(s[i+1]))
    elif s[i]=="double":
        print(word_to_digit(s[i+1]))
    else:
        print(word_to_digit(s[i]))