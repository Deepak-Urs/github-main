def maxSumOfSubArrSizeK(arr, k):
    i = 0
    j = 0
    size = len(arr)
    sm = 0
    res = 0

    while j < size:
        sm += arr[j]
        w = j-i+1
        
        if w < k:
            j += 1
        elif w == k:
            res = max(res, sm)

            sm -= arr[i]
            i += 1
            j += 1
    
    return res


print(maxSumOfSubArrSizeK([2,5,1,8,2,9,1], 3))