def binSearchUnkOrd(arr, t):
    st = 0
    en = len(arr)-1
    isAsc = True if arr[0] < arr[1] else False
    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]: return m
        elif t < arr[m]: 
            if isAsc:
                en = m - 1
            else:
                st = m + 1
        elif t > arr[m]: 
            if isAsc:
                st = m + 1
            else:
                en = m - 1

    return -1

print(binSearchUnkOrd([5,4,3,2,1], 2))
print(binSearchUnkOrd([1,2,3,4,5], 2))