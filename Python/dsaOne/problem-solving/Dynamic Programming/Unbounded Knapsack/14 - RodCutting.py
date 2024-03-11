def rodCutting(Lt, Pr, L, n):
    r = n+1
    c = L + 1
    res = [[] for ix in range(r)]

    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0: res[i].append(0)
            else: res[i].append(None)

    for i in range(1,r):
        for j in range(1,c):
            if Lt[i-1] <= j:
                res[i][j] = max(res[i-1][j], Pr[i-1] + res[i][j-Lt[i-1]])
            elif Lt[i-1] > j:
                res[i][j] = res[i-1][j]

    for ix in res:
        print(ix)
    
    return res[i][j]

Lt = [1,2,3,4,5,6,7,8]
Pr = [1,5,8,9,10,17,17,20]
L = 8
n = len(Lt)
print(rodCutting(Lt, Pr, L, n))