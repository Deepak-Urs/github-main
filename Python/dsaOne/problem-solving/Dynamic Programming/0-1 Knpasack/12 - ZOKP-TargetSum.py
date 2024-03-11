def ZOKPTargetSum(arr, sm):
    r = len(arr) + 1
    c = sm + 1
    res = [[] for i in range(r)]

    for i in range(r):
        for j in range(c):
            if (i == 0 and j == 0) or j == 0: res[i].append(1)
            elif i == 0: res[i].append(0)
            else: res[i].append(None)
    
    for i in range(1,r):
        for j in range(1,c):
            if arr[i-1] <= j:
                res[i][j] = res[i-1][j] + res[i-1][j-arr[i-1]]
            elif arr[i-1] > j:
                res[i][j] = res[i-1][j]
    
    return res[i][j]


def main(arr, diff):
    sm = (diff + sum(arr))//2
    return ZOKPTargetSum(arr, sm)

print(main([1,1,2,3], 1))
