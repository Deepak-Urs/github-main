def shortestCommonSuperSequence(X, Y, m, n):
    r = m + 1
    c = n + 1
    t = [[] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0: t[i].append(0)
            else: t[i].append(None)
    
    for i in range(1, r):
        for j in range(1, c):
            if X[i-1] == Y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            elif X[i-1] != Y[j-1]:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    
    l = t[i][j]

    return m + n - l

X = 'aggtab'
Y = 'gxtxayb'
print(shortestCommonSuperSequence(X, Y, len(X), len(Y)))


