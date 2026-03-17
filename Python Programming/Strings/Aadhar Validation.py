aad=input()
l=len(aad)
if l==12 or l==14:
    if l==12:
        c=0
        for i in aad:
            asi=ord(i)
            if asi>=48 and asi<=57:
                c+=1
            else:
                print("Invalid aadhar")
                break
        if c==12:
            print("Valid aadhar")
    else:
        c=0
        for i in range(0,l):
            asi=ord(aad[i])
            if (i==4 or i==9) and aad[i]==" ":
                c+=1
            elif i!=4 and i!=9 and asi>=48 and asi<=57:
                c+=1
            else:
                print("Invalid aadhar")
                break
        if c==14:
            print("Valid aadhar")
else:
    print("Invalid aadhar")