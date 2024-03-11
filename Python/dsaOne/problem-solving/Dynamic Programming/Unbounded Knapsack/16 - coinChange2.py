def coinChange2(Cn,sm):
    r = len(Cn) + 1
    c = sm + 1
    res = [[] for ix in range(r)]

    for i in range(r):
        for j in range(c):
            if i == 0: res[i].append(float('inf'))
            elif j == 0 and i != 0: res[i].append(0)
            else: res[i].append(None)

    for j in range(1, len(res[1])):
        if j % Cn[0] == 0:
            res[1][j] = j/Cn[0]
        else:
            res[1][j] = float('inf')

    for i in range(1,r):
        for j in range(1,c):
            if Cn[i-1] <= j:
                res[i][j] = min(res[i-1][j], 1+res[i][j-Cn[i-1]])
            elif Cn[i-1] > j:
                res[i][j] = res[i-1][j]
    
    for i in range(r):
        print(res[i])
    return res[i][j]

print(coinChange2([2,3,5], 5))
