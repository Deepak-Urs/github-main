# here arr is in sorted order, we do not know if it is ascending or descending
def orderUnkBinSearch(arr, t):
    isAsc = None
    if arr[0] < arr[1]:
        isAsc = True
    else:
        isAsc = False

    st = 0
    en = len(arr)-1

    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            return m
        if t < arr[m]:
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
    
print(orderUnkBinSearch([1,2,3,4,5,6,7,8,9], 4))
print(orderUnkBinSearch([91,82,73,64,55,46,37,28,19], 37))

