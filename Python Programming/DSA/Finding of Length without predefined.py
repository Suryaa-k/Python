def find_length(arr):
    count = 0
    i = 0
    while i < 10**18:   # large number to simulate "infinite"
        try:
            arr[i]
            count += 1
            i += 1
        except IndexError:
            break
    return count

#or

def find_length(arr):
    count = 0
    i = 0
    while True:
        try:
            arr[i]
            count += 1
            i += 1
        except IndexError:
            break
    return count

#or

def find_length(arr, i=0):
    try:
        arr[i]
        return 1 + find_length(arr, i + 1)
    except IndexError:
        return 0