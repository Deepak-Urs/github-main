def findPeakEle(arr):
    st,en,il = 0, len(arr)-1, len(arr)-1

    while st <= en:
        m = st + (en-st)//2

        if m > 0 and m < il:
            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return arr[m]
            elif arr[m-1] > arr[m]:
                en = m - 1
            else:
                st = m + 1
        elif m == 0:
            return arr[m] if arr[m] > arr[m+1] else arr[m+1]
        else:
            return arr[il] if arr[il] > arr[il-1] else arr[il-1]

    return -1

print(findPeakEle([55,30,10,20,15]))
    
