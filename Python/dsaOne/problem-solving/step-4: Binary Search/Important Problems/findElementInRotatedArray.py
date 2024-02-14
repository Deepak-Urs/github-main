def binSearch(arr, st, en, t):
    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            return m
        elif t <= arr[m]:
            en = m - 1
        else:
            st = m + 1

    return -1

def findElementInRotatedArray(arr, t):
    st = 0
    en = len(arr)-1
    l = len(arr)
    idx = -1

    while st <= en:
        m = st + (en-st)//2
        next = (m+1)%l
        prev = (m+l-1)%l

        if arr[m] <= arr[prev] and arr[m] <= arr[next]:
            idx = m
            break
        elif arr[en] <= arr[m]:
            st = m + 1
        else:
            en = m - 1
        
    r1 = binSearch(arr, 0, idx-1, t)
    r2 = binSearch(arr, idx, l-1, t)

    if r1 == -1 and r2 == -1:
        return -1
    else:
        if r1 != -1:
            return r1
        else:
            return r2
        
    
print(findElementInSortedArray([11,12,15,18,2,6,8,10], 15))