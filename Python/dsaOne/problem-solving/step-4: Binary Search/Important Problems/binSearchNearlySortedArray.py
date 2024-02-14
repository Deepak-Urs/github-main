def binSearchNearlySortedArray(arr, t):
    st = 0
    en = len(arr)-1

    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            return m
        elif st <= m-1 and t == arr[m-1]:
            return m-1
        elif m+1 <= en and t == arr[m+1]:
            return m+1
        elif t <= arr[m]:
            en = m - 2
        else:
            st = m + 2

    return -1

print(binSearchNearlySortedArray([5,10,30,20,40], 40))