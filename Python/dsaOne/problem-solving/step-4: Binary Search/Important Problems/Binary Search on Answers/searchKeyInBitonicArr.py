def binSearch(arr, st, en, k,  isAsc):
    while st <= en:
        m = st + (en-st)//2

        if k == arr[m]:
            return m
        elif k < arr[m]:
            if isAsc:
                en = m - 1
            else:
                st = m + 1
        else:
            if isAsc:
                st = m + 1
            else:
                en = m - 1
    
    return -1

def searchKeyInBitonicArr(arr, k):
    st = 0
    en = len(arr)-1
    il = en
    peak = -1

    while st <= en:
        m = st + (en-st)//2

        if m > 0 and m < il:
            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                peak = m
                break
            elif arr[m] < arr[m+1]:
                st = m + 1
            else:
                en = m - 1
        elif m == 0:
            peak = arr[m] if arr[m] > arr[m+1] else arr[m+1]
        elif m == il:
            peak = arr[m] if arr[m] > arr[m-1] else arr[m-1]
    
    r1 = binSearch(arr, 0, peak-1, k,  True)
    r2 = binSearch(arr, peak, il, k, False)

    if r1 == -1 and r2 == -1:
        return -1
    else:
        return r1 if r1 != -1 else r2
    
print(searchKeyInBitonicArr([1,4,5,7,12,8,3,2], 3))