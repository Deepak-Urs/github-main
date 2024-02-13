def binarySearch(arr, t):
    start = 0
    end = len(arr)-1

    while(start <= end):
        #mid = (start + end)//2
        # enhancemenet to avoid overflow
        mid = start + (end-start)//2

        if t == arr[mid]:
            return mid
        elif t < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        
    return -1

print(binarySearch([1,2,3,4,5,6,7,8,9], 7))
print(binarySearch([1,2,3,4,5,6,7,8,9], 10))