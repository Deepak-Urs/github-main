def largestSubArrayWithSumK(arr, k):
    l = 0
    r = 0
    n = len(arr)
    sum = arr[0]
    maxlen = 0

    while r < n:
        while l <=r and sum > k:
            sum -= arr[l]
            l += 1

        if sum == k:
            maxlen = max(maxlen, r-l+1)
        
        r += 1
        if r < n: sum += arr[r]

    return maxlen

print(largestSubArrayWithSumK([1, 2, 3, 1, 1, 1, 1], 3))
print(largestSubArrayWithSumK([2, 2, 4, 1, 2], 1))
