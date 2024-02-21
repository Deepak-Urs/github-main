# 1 3 2 4
def nearestGreaterValueToRight(arr):
    res = []
    stk = []
    
    for i in range(len(arr)-1, -1, -1):
        if len(stk) == 0:
            res.append(-1)
        elif len(stk) > 0 and stk[-1] > arr[i]:
            res.append(stk[-1])
        elif len(stk) > 0 and stk[-1] <= arr[i]:
            while len(stk) > 0 and stk[-1] <= arr[i]:
                stk.pop()
            if len(stk) == 0:
                res.append(-1)
            else:
                res.append(stk[-1])

        stk.append(arr[i])
    
    r2 = [res[i] for i in range(len(res)-1, -1, -1)]
    return r2

print(nearestGreaterValueToRight([1,3,2,4]))