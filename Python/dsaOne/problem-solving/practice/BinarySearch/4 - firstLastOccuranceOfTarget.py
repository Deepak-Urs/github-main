def firstLastOccuranceOfTarget(arr, t):
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
    print('first occurance index of target - ', res)
    
    
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
    print('last occurance index of target - ', res)



print(firstLastOccuranceOfTarget([2,4,10,10,10,18,20], 10))