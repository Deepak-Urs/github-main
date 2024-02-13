def firstAndLastOccurance(arr, t):
    st = 0
    en = len(arr)-1
    res = -1

    #First Occurance 
    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            res = m
            en = m - 1
        elif t < arr[m]:
            en = m - 1
        else:
            st = m + 1
    print('First Occurance at index-', res)

    st = 0
    en = len(arr)-1
    res = -1

    #Last Occurance
    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            res = m
            st = m + 1
        elif t < arr[m]:
            en = m - 1
        else:
            st = m + 1
    print('Last Occurance at index-', res)

firstAndLastOccurance([2,4,10,10,10,18,20], 10)
firstAndLastOccurance([2,4,10,18,20], 10)
