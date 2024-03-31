def findEleInRotatedArr(arr, t):
    st = 0
    en = len(arr)-1
    l = en + 1
    idx = -1

    while st <= en:
        m = st + (en-st)//2
        prev = (m+l-1)%l
        next = (m+1)%l

        if arr[m] <= arr[prev] and arr[m] <= arr[next]:
            idx = m
            break
        elif arr[m] <= arr[en]:
            en = m - 1
        else:
            st = m + 1
    
    lB = binSearch(arr, 0, idx-1, t)
    rB = binSearch(arr, idx, l-1, t)

    if lB == -1 and rB == -1:
        return -1
    else:
        if lB == -1:
            return rB
        else:
            return lB

def binSearch(arr, st, en, t):
    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]: return m
        elif t < arr[m]: en = m - 1
        elif t > arr[m]: st = m + 1

    return -1


print(findEleInRotatedArr([11,12,15,18,2,6,8,10], 15))