# 6.  Use filter() to remove all vowels from a string and print the final string
# x = input("Enter a String: ")

l = ['a','e','i','o','u','A','E','I','O','U']
li = list(filter(lambda x:not x in l, x))
print("".join(li))