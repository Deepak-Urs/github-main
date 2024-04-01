def findElePosInInfArr(arr, t):
    st = 0
    en = 1

    while arr[en] < t:
        st = en
        en *= 2
    
    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            return m
        elif t < arr[m]:
            en = m - 1
        else:
            st = m + 1
    
    return -1

print(findElePosInInfArr([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 10))