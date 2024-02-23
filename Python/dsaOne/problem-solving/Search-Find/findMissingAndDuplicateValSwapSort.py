def findMissingAndDuplicateValSwapSort(arr):
    size = len(arr)
    dup = -1
    mis = -1
    res = []

    for i in range(size):
        if arr[i] == i+1 :
            continue
        else:
            swpIdx = arr[i]-1
            temp = arr[i]
            arr[i] = arr[swpIdx]
            arr[swpIdx] = temp
    
    for j in range(size):
        if arr[j] != j+1:
            mis = j+1
            dup = arr[j]
            res.append((mis, dup))
    
    return [arr, res]

print(findMissingAndDuplicateValSwapSort([1,7,3,4,5,6,4,7,9]))
print(findMissingAndDuplicateValSwapSort([2,3,1,8,2,3,5,1]))


