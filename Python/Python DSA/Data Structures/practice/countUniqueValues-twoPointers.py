def countUniqueValues(arr):
    if len(arr) == 0:
        return 0
    
    count = 0
    hm = {}

    l = 0
    r = len(arr)-1

    # for i in range(0, len(arr)-1):
    while l < r:
        # else:
        if arr[l] not in hm:
            hm[arr[l]] = 1
            l += 1
            count += 1
        elif arr[r] not in hm:
            hm[arr[r]] = 1
            r -= 1
            count += 1
        elif arr[l] in hm:
            l += 1
        elif arr[r] in hm:
            r -= 1
            
    return count

print(countUniqueValues([1,1,1,1,1,2])) #2
print(countUniqueValues([1,2,3,4,4,4,7,7,12,12,13])) #7
print(countUniqueValues([])) #0
print(countUniqueValues([-2,-1,-1,0,1])) #4