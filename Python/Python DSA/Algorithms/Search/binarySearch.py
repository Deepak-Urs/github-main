import math

def binarySearch(array, value):
    left = 0
    right = len(array) - 1
    middle = math.floor( (left + right) / 2 )

    while array[middle] != value and left <= right:
        if value < array[middle]:
            right = middle - 1
        elif value > array[middle]:
            left = middle + 1

        middle = math.floor( (left + right) / 2 )

    if array[middle] == value:
        return middle
    else:
        return -1

print(binarySearch([1,2,3,4,5,6,7], 5))
print(binarySearch([1,2,3,4,5,6,7], 9))