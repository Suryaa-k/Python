# 1. Use map() with a lambda to add 5 to every element of the following nested
# list [[1, 2], [3, 4], [5, 6]]

k = [[1, 2], [3, 4], [5, 6]]
li = list(map(lambda x: [i+5 for i in x], k))
print(li)