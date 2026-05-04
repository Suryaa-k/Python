def max_unique_sublist_sum(lst, k):
    max_sum = 0

    for i in range(len(lst) - k + 1):
        sublist = lst[i:i+k]

        if len(sublist) == len(set(sublist)):
            max_sum = max(max_sum, sum(sublist))
    return max_sum

my_list = [1, 5, ]
print(max_unique_sublist_sum(my_list, 3))
