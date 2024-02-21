def maxAreaHistogram(arr):
    # nsl
    # nsr
    # res basd on indexes

    stk = []
    res = []
    size = len(arr)
    psIdx = -1

    for i in range(size):
        if len(stk) == 0:
            res.append(psIdx)
        elif len(stk) > 0 and stk[-1][0] < arr[i]:
            res.append(stk[-1][1])
        elif len(stk) > 0 and stk[-1][0] >= arr[i]:
            while len(stk) > 0 and stk[-1][0] >= arr[i]:
                stk.pop()
            if len(stk) == 0:
                res.append(psIdx)
            else:
                res.append(stk[-1][1])
        
        stk.append([arr[i], i])

    nsl = res

    stk = []
    res = []
    psIdx = size

    for i in range(size-1, -1, -1):
        if len(stk) == 0:
            res.append(psIdx)
        elif len(stk) > 0 and stk[-1][0] < arr[i]:
            res.append(stk[-1][1])
        elif len(stk) > 0 and stk[-1][0] >= arr[i]:
            while len(stk) > 0 and stk[-1][0] >= arr[i]:
                stk.pop()
            if len(stk) == 0:
                res.append(psIdx)
            else:
                res.append(stk[-1][1])
        
        stk.append([arr[i], i])
    
    nsr = [res[i] for i in range(size-1, -1, -1)]

    width = []
    for i in range(0, len(arr)):
        width.append(nsr[i] - nsl[i] - 1)

    area = []
    for i in range(len(arr)):
        area.append(arr[i]*width[i])
    
    return max(area)


#print(maxAreaHistogram([6,2,5,4,5,1,6]))

