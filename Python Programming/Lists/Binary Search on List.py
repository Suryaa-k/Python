# 17 Write a program to perform binary search on a sorted list.

def binary_search(l, value):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == value:
            return mid
        elif l[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
l=list(map(int,input().split()))
value=int(input())
result = binary_search(l, value)
if result != -1:
    print(f"Element {value} found at index {result}")
else:
    print(f"Element {value} not found")