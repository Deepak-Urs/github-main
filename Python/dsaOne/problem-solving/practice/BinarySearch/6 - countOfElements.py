def countOfElements(arr, t):
    st, en = 0, len(arr)-1
    res = -1

    while st <= en:
        m = st + (en-st)//2
        if t == arr[m]:
            res = m
            en = m - 1
        elif t < arr[m]:
            en = m - 1
        else:
            st = m + 1
    
    f = res
    st, en = 0, len(arr)-1

    while st <= en:
        m = st + (en-st)//2
        if t == arr[m]:
            res = m
            st = m + 1
        elif t < arr[m]:
            en = m - 1
        else:
            st = m + 1

    l = res

    return l-f+1

print(countOfElements([2,4,10,10,18,20], 10 ))