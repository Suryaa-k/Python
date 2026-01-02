# 5. Use map() on a string to convert each character into its ASCII value (using ord()). Print the result list.

st = input("Enter a text: ")
li = list(map(ord, st))
print(li)