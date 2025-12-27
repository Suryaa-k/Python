# Write a function named find_length(obj) that uses a loop to calculate the 
# length of the given object without using the built-in len() function. The 
# function should return the calculated length if the object is iterable. If a 
# non-iterable object such as an integer is passed, the function should raise and 
# handle a TypeError, and print an appropriate error message explaining what 
# happens when an integer is sent as input.

def find_len(li):
    if isinstance(li,(list,set,dict)):
        i=0
        while True:
            i+=1
            li.pop()
    elif isinstance(li,(str,tuple,frozenset)):
        if isinstance(li,str):
            i=0
            while True:
                li[i]
                i+=1
        else:
            k=0
            for j in li:
                k+=1
            raise IndexError(f"{i}")
    else:
        raise TypeError("Non Sequential Value Given")
try:
    k=find_len("String")
    l=find_len({'a':1,'b':2})
    m=find_len(35)
except Exception as e:
    print(e)
