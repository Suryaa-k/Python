#Write a program to find out LCM of two given numbers (Least Common Multiple)

n1=int(input("Enter Number 1: "))
n2=int(input("Enter Number 2: "))
mul=1
while True:
    if mul%n1==0 and mul%n2==0:
        print(mul)
        break 
    mul+=1
