# length of every value's (i - NGL index)

# 100,80,60,70,60,75,85
# 1,1,1,2,1,4,6
def stockSpan(arr):
    stk = []
    res = []

    for i in range(len(arr)):
        if len(stk) == 0:
            res.append(-1)
        elif len(stk) > 0 and stk[-1][0] > arr[i]:
            res.append(stk[-1][1])
        elif len(stk) > 0 and stk[-1][0] <= arr[i]:
            while len(stk) > 0 and stk[-1][0] <= arr[i]:
                stk.pop()
            if len(stk) == 0:
                res.append(-1)
            else:
                res.append(stk[-1][1])

        stk.append([arr[i], i])
    
    for i in range(len(res)):
        res[i] = i - res[i]
    
    return res

print(stockSpan([100,80,60,70,60,75,85]))
