def rainWaterTrapping(arr):
    # maxL
    # maxR
    # area[i] = min(mxL[i]-mxR[i]) - arr[i]
    # return sum(area)
    size = len(arr)
    maxL = [0 for ix in range(size)]
    maxR = [0 for jx in range(size)]

    mL = arr[0]
    for i in range(size):
        maxL[i] = max(mL, arr[i])

    mR = arr[-1]
    for j in range(size-1, -1, -1):
        maxR[j] = max(mR, arr[j])

    area = []
    for k in range(size):
        area.append(min(maxL[k], maxR[k]) - arr[k])
    
    return sum(area)

print(rainWaterTrapping([3,0,0,2,0,4]))

    