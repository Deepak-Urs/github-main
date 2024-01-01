def getLongestSubArray(arr, k):
    n = len(arr)
    l = 0

    for i in range(n):
        for j in range(i,n):
            s = 0
            for k in range(i, j+1):
                s += arr[k]
            
            if s == k:
                l = max(l, j-i+1)
    
    return l

print(getLongestSubArray([1,2,1,0,1], 4))
print(getLongestSubArray([-50, 0, 52], 2))