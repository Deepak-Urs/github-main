def findLargest(arr):
    l = 0
    r = len(arr)-1
    mx = -1

    while l < r:
        if arr[l] > arr[r]:
            m2 = arr[l]
        else:
            m2 = arr[r]
        mx = max(m2,mx)
        l += 1
        r -= 1
    
    return mx
    # direct method -> return max(arr)

print(findLargest([1,3,4,2,7,9]))