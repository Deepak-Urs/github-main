def countOfElements(arr, t):
    st, en = 0, len(arr)-1
    res = -1

    # first occurance
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
    res = -1

    # last occurance
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

    if f == -1 or l == -1: return 1
    elif f == -1 and l == -1: return 0
    else: return l - f + 1

print(countOfElements([2,4,10,10,10,18,20], 10))