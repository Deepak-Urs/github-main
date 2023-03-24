def binarySearch(arr, val):
    l , r  = 0, len(arr)-1

    while l <=r:
        mid = (l + r)//2
        if arr[mid] < val:
            l = mid
        elif arr[mid] > val:
            r = mid
        else:
            return mid
    
    return -1
        
    
print(binarySearch([1,2,3,4,5,6,7,8,9], 7))