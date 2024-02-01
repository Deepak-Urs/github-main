def maxNum(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n-1], maxNum(arr, n-1))

print(maxNum([4,12,11,7], 4))