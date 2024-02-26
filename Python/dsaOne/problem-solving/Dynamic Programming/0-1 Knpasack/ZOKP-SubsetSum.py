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

    for ix in res:
        print(ix)

    return res[i][j]


print(ZOKPSubsetSum([2,3,7,8,10], 11))