def ZOKPSubsetSum(arr, sm):
    # initialization
    r = len(arr)+1
    c = sm+1
    res = [[] for ix in range(r)]
    for i in range(len(res)):
        for j in range(c):
            if i == 0 and j == 0: res[i].append(True)
            elif j == 0: res[i].append(True)
            elif i == 0: res[i].append(False)
            else: res[i].append(None)

    # finding result
    for i in range(1, r):
        for j in range(1, c):
            if arr[i-1] <= j:
                res[i][j] = res[i-1][j-arr[i-1]] or res[i-1][j]
            elif arr[i-1] > j:
                res[i][j] = res[i-1][j]

    #for ix in res:
    #    print(ix)

    return res[r-1]

ar = [1,2,7]
smm = 10
def ZOKPMinimumSubsetSum(arr, sm):
    rnge = sm
    result = float('inf')
    resultArray = ZOKPMinimumSubsetSum(arr, rnge//2)
    print(resultArray)

    for j in range(len(resultArray)):
        if resultArray[j]:
            result = min(result, rnge-2*j)
            
    

    return result
    




    # for every val in ans range, calc the res[]
    # pick up the last row of the res and run a loop with formaula r = min(rnge-2ss[i], r)
    # return r

print(ZOKPMinimumSubsetSum(ar, smm))
#print(ZOKPMinimumSubsetSum([2,3,7,8,10], 11))