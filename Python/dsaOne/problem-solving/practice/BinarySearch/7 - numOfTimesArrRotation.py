def numOfTimesArrRotation(arr):
    st, en, l = 0, len(arr)-1, len(arr)

    while st <= en:
        m = st + (en-st)//2
        prev = (m+l-1)%l
        next = (m+1)%l

        if arr[m] <= arr[prev] and arr[m] <= arr[next]:
            return m
        elif arr[m] <= arr[en]:
            en = m - 1
        else:
            st = m + 1
    
    return -1

print(numOfTimesArrRotation([11,12,15,1,2,5,6,8]))