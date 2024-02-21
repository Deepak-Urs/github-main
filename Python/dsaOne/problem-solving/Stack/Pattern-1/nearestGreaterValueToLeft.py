
def nearestGreaterValueToLeft(arr):
    res = []
    stk = []
    
    for i in range(len(arr)):
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
    
    return res

print(nearestGreaterValueToLeft([1,3,2,4]))