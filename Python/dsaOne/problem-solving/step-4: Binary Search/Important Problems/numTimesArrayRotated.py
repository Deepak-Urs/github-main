def numTimesArrayRotated(arr):
    st = 0
    en = len(arr)-1
    l = len(arr)

    while st <= en:
        m = st + (en-st)//2
        next = (m+1)%l
        prev = (m+l-1)%l

        if arr[m] <= arr[prev] and arr[m] <= arr[next]:
            return m
        elif arr[en] <= arr[m]:
            st = m + 1
        else:
            en = m - 1

    return -1

print(numTimesArrayRotated([11,12,15,18,2,5,6,8]))

