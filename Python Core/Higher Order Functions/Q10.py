# 10.  Given a list of numbers: [5, 10, 15, 20, 25, 30]
# Perform the following in a single pipeline:
# • Use map() to square each number
# • Use filter() to keep only numbers divisible by 5
# • Use reduce() to calculate the sum of remaining numbers

from functools import reduce
l = [5, 10, 12, 20, 18, 26]
li = reduce(lambda x,y: x+y,list(filter(lambda x: x%5==0,list(map(lambda x:x*x, l)))))
print(li)