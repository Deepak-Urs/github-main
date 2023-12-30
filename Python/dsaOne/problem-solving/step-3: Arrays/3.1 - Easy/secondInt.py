#def secondInt(arr):
#    arr = sorted(arr)
#    print(arr)
#    return [arr[1], arr[-2]]
#print(secondInt([2,1,4,3,5]))


import math
def secondIntBetter(arr):
    mx = -math.inf
    mn = math.inf
    smx = -math.inf
    smn = math.inf

    for i in arr:
        if i < mn:
            mn = i
        if i > mx:
            mx = i

    for i in range(len(arr)):
        if arr[i] < smn and arr[i] != mn:
            smn = arr[i]
        if arr[i] > smx and arr[i] != mx:
            smx = arr[i]
    
    return [smn, smx]


print(secondIntBetter([2,1,4,3,5]))