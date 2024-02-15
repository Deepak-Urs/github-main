def peakElement(arr):
    st = 0
    en = len(arr)-1
    il = len(arr)-1

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
            if arr[m] > arr[m+1]:
                return arr[m]
            else:
                return arr[m+1]
        elif m == il:
            if arr[m] > arr[m-1]:
                return arr[m]
            else:
                return arr[m-1]

    return -1


print(peakElement([5,10,20,15]))
#print(peakElement([5,10,20,15,7,19,12])) may need a recursive approach after pivot of m