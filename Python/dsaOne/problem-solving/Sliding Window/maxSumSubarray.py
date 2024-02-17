def maxSumSubArray(arr, w):
    i = 0
    j = 0
    size = len(arr)
    summ = 0
    mx = -1

    while j < size:
        summ += arr[j]
        ws = j-i+1

        if ws < w:
            j += 1
        elif ws == w:
            mx = max(summ, mx)
            summ -= arr[i]
            i += 1
            j += 1
    
    return mx

print(maxSumSubArray([2,5,1,8,2,9,1], 3))
