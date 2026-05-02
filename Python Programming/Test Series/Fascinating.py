# Fascinating Number

n=int(input())
n=abs(n)
l=[]
if n==0:
    print("Invalid")
elif n<100:
    print("Invalid Input")
else:
    s=f"{n}{n*2}{n*3}"
print(s)

for i in range(1,10):
    if str(i) not in (s):
            print("Not")
            break
else:
    print("Fas")