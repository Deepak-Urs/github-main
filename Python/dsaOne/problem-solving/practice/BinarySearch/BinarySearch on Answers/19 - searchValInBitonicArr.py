def binSearch(arr, st, en, t):
    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            return m
        elif t < arr[m]:
            en = m - 1
        else:
            st = m + 1
    return -1

def searchValInBitonicArr(arr, t):
    st,en,il = 0, len(arr)-1, len(arr)-1
    res = -1

    while st <= en:
        m = st + (en-st)//2

        if m > 0 and m < il:
            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                res = m
                break
            elif arr[m-1] > arr[m]:
                en = m - 1
            else:
                st = m + 1
        elif m == 0:
            return arr[m] if arr[m] > arr[m+1] else arr[m+1]
        else:
            return arr[il] if arr[il] > arr[il-1] else arr[il-1]

    s1 = binSearch(arr, 0 , res, t)
    s2 = binSearch(arr, res+1 , il, t)

    if s1 == -1 and s2 == -1: return -1
    else:
        if s1 == -1: return s2
        else: return s1

print(searchValInBitonicArr([1,4,7,12,10,2], 10))
    
