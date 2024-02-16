def findMaxEleInBitonicArray(arr):
    st = 0
    en = len(arr)-1
    il = en

    while st <= en:
        m = st + (en-st)//2

        if m > 0 and m < il:
            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return arr[m]
            elif arr[m] < arr[m+1]:
                st = m + 1
            else:
                en = m - 1
        elif m == 0:
            return arr[m] if arr[m] > arr[m+1] else arr[m+1]
        else:
            return arr[m] if arr[m] > arr[m-1] else arr[m-1]
    
    return -1

print(findMaxEleInBitonicArray([1,4,7,12,19,4,2]))