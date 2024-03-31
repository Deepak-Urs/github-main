def binSearchNearlySorted(arr, t):
    st, en = 0, len(arr)-1
    
    while st <= en:
        m = st + (en - st)//2

        if t == arr[m]: return m
        elif t == arr[m-1] and st <= m-1: return m - 1
        elif t == arr[m+1] and en >= m+1: return m + 1
        elif t <= arr[m]: en = m - 1
        else: st = m + 1

    return -1


print(binSearchNearlySorted([5,10,30,20,40], 20))