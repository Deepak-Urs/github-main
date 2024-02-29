def coinChange1(Cn, sm):
    r = len(Cn) + 1
    c = sm + 1
    res = [[] for i in range(r)]
    
    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0: res[i].append(1)
            elif i == 0: res[i].append(0)
            elif j == 0: res[i].append(1)
            else: res[i].append(None)
    
    for i in range(1,r):
        for j in range(1, c):
            if Cn[i-1] <= j:
                res[i][j] = res[i-1][j] + res[i][j-Cn[i-1]]
            elif Cn[i-1] > j:
                res[i][j] = res[i-1][j]
    
    for i in range(r):
        print(res[i])
    return res[i][j]

print(coinChange1([1,2,2], 5))
