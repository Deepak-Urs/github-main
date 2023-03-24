def averagePair(arr, avg):
    l, r = 0, len(arr)-1
    res = False

    if len(arr) == 0:
        return res

    idx = 1
    while l < r:
        tempAvg = (arr[l] + arr[r])/2
        if tempAvg < avg:
            l += 1
        elif tempAvg > avg:
            r -= 1
        else:
            res = True
            break
    
    return res

print(averagePair([1,2,3],2.5)) # true
print(averagePair([1,3,3,5,6,7,10,12,19],8)) # true
print(averagePair([-1,0,3,4,5,6], 4.1)) # false
print(averagePair([],4)) # false