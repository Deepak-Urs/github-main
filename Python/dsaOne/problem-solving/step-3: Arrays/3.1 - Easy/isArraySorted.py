def isArraySorted(arr):
    if len(arr) == 0: return False
    elif len(arr) == 1: return True

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    
    return True

print(isArraySorted([1,2,3,4,5]))
print(isArraySorted([5,4,3,2,1]))