def findFirstOccuranceOfTarget(arr, t):
    st = 0
    en = 1
    res = -1

    while arr[en] < t:
        st = en
        en *= 2
    
    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            res = m
            en = m - 1
        elif t < arr[m]:
            en = m - 1
        else:
            st = m + 1
    
    return res

print(findFirstOccuranceOfTarget([0,0,0,1,1,1,1,1], 1))