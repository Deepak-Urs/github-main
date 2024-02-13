def countElementSortedArr(arr, t):
    st = 0
    en = len(arr)-1
    first = -1

    #LHS Occurance counting
    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            first = m
            en = m - 1
        elif t < arr[m]:
            en = m - 1
        else:
            st = m + 1

    st = 0
    en = len(arr)-1
    last = -1

    #RHS Occurance counting
    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            last = m
            st = m + 1
        elif t < arr[m]:
            en = m - 1
        else:
            st = m + 1
    
    return last-first+1

print(countElementSortedArr([2,4,10,10,10,18,20], 10))
print(countElementSortedArr([2,4,10,18,20], 10))
