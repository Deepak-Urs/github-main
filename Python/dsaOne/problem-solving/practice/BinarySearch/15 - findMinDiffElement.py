def findMinDiffElement(arr, t):
    st, en = 0, len(arr)-1

    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            return t
        elif t < arr[m]:
            en = m - 1
        else:
            st = m + 1
    
    return arr[st] if abs(arr[st] - t) <= abs(arr[en] - t) else arr[en]

print(findMinDiffElement([1,3,8,10,15], 14))
        
