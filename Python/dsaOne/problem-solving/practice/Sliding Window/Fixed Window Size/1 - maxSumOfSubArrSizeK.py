def maxSumOfSubArrSizeK(arr, k):
    i = 0
    j = 0
    size = len(arr)
    sm = 0
    res = 0

    while j < size:
        sm += arr[j]
        ws = j-i+1

        if ws < k:
            j += 1
        elif ws == k:
            res = max(res, sm)
            sm -= arr[i]

            j += 1
            i += 1
    
    return res

print(maxSumOfSubArrSizeK([2,5,1,8,2,9,1], 3))