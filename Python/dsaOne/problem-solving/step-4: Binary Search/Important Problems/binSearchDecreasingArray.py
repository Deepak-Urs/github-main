def binSearchDecreasingArray(arr, t):
    st = 0
    en = len(arr)-1

    while (st <= en):
        m = st + (en-st)//2
        
        if t == arr[m]:
            return m
        elif t < arr[m]:
            st = m + 1
        else:
            en = m - 1

    return -1

print(binSearchDecreasingArray([10,9,8,7,6,5,4,3,2,1], 7))