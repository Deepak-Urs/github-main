def findMissingAndDuplicateVal(arr):
    size = len(arr)
    oToNArr = [i+1 for i in range(size)] # 1toN arr

    # m - d
    sumM = sum(oToNArr)
    sumD = sum(arr)
    eq1 = sumM - sumD

    # m^2 - d^2
    ssM = 0
    for i in oToNArr:
        ssM += i*i
        print(ssM)

    ssD = 0
    for j in arr:
        ssD += j*j
        print(ssD)
    
    eq2 = ssM - ssD

    # m + d
    mPd = eq2/eq1

    # m from 2m
    m = (eq1 + mPd)//2
    d = mPd - m

    print('Missing Number: ', int(m))
    print('Duplicate Number:', int(d))

findMissingAndDuplicateVal([1,4,3,4,5])


