import math
def highLowFrequency(arr):
    hm = {}
    for i in arr:
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 1
    
    minVal = math.inf
    maxVal = -math.inf
    
    for i in hm:
        if hm[i] < minVal:
            minVal = hm[i]
            minEle = i
        if hm[i] > maxVal:
            maxVal = hm[i] 
            maxEle = i 
    
    print('min. Frequency value = ', minEle)
    print('max. Frequency value = ', maxEle)

highLowFrequency([10,5,10,15,15,15,15,10,5])
