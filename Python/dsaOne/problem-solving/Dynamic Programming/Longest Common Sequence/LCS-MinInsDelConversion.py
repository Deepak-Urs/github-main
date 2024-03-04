def minInsDelsConversion(X, Y):
    r = len(X) + 1
    c = len(Y) + 1
    res = [[] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0: res[i].append(0)
            else: res[i].append(None)
    
    for i in range(1, r):
        for j in range(1, c):
            if X[i-1] == Y[j-1]:
                res[i][j] = 1 + res[i-1][j-1]
            elif X[i-1] != Y[j-1]:
                res[i][j] = max(res[i-1][j], res[i][j-1])
    
    print('LCS: ', res[i][j])
    rm = len(X)-res[i][j] if r > c else len(Y)-res[i][j]
    ins = len(Y)-res[i][j] if r > c else len(X)-res[i][j]
    print('Min. num. of deletions: ', rm)
    print('Min. num. of insertions: ', ins)

x = 'heap'
y = 'pea'
minInsDelsConversion(x, y)