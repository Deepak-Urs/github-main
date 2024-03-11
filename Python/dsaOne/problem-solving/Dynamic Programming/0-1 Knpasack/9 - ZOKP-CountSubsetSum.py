def ZOKPCountSubsetSum(arr, sm):
    r = len(arr)+1
    c = sm + 1
    res = [[] for ix in range(r)]
    

    for i in range(r):
        for j in range(c):
            if (i == 0 and j == 0): res[i].append(1)
            elif i == 0: res[i].append(0)
            elif j == 0: res[i].append(1)
            else: res[i].append(None)
    
    for i in range(1,r):
        for j in range(1,c):
            if arr[i-1] <= j:
                res[i][j] = res[i-1][j-arr[i-1]] + res[i-1][j]
            else:
                res[i][j] = res[i-1][j]
    
    for i in range(r):
        print(res[i])
    return res[i][j]

print(ZOKPCountSubsetSum([2,3,5,8,10], 10))
