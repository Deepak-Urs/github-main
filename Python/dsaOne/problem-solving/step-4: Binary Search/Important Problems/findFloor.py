def findFloorOfTarget(arr, t):
    st = 0
    en = len(arr)-1
    res = -1

    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            return arr[m]
        elif t < arr[m]:
            en = m - 1
        else:
            # since arr[m] now becomes a candidate for floor value
            res = arr[m]
            st = m + 1

    return res

print(findFloorOfTarget([1,2,3,4,8,10,12,19], 5))