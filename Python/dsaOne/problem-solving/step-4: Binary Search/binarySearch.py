def binarySearch(arr, t):
    l = 0
    r = len(arr)-1

    while(l <= r):
        m = (l+r)//2

        if arr[m] == t: return m
        elif t > arr[m]:
            l = m+1
        else:
            r = m-1

    return -1

print(binarySearch([1,2,3,4,5,6,7,8,9], 6))
print(binarySearch([1,2,3,4,5,6,7,8,9], 3))