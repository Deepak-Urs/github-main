def findNextAB(arr, t):
    st = 0
    en = len(arr)-1
    res = ''

    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            st = m + 1
        elif t < arr[m]:
            res = arr[m]
            en = m - 1
        else:
            st = m + 1
    
    return res

print(findNextAB(['a', 'b', 'f', 'h', 'i', 'm'], 'g'))
