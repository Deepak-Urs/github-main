def singleNumber(arr):
    # approach-1
    #hm = {}

    #for i in arr:
    #    if i in hm:
    #        hm[i] += 1
    #    else:
    #        hm[i] = 1

    #for i in hm:
    #    if hm[i] == 1:
    #        return i

    # approach-2
    xxor = 0
    for i in arr:
        xxor ^= i
        print(xxor)
    return xxor

print(singleNumber([4,1,2,1,2]))
#print(singleNumber([2,2,1]))
        
