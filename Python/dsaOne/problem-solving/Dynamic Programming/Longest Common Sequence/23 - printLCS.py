def printLCS(X, Y, m, n):
    r = m + 1
    c = n + 1
    res = [[] for _ in range(r)]
    #mx = 0
    st = ''
    #isC = False
    #stR = []

    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0: res[i].append(0)
            else: res[i].append(None)
    
    for i in range(1,r):
        for j in range(1,c):
            if X[i-1] == Y[j-1]:
                res[i][j] = 1 + res[i-1][j-1]
            elif X[i-1] != Y[j-1]:
                res[i][j] = max(res[i-1][j], res[i][j-1])
    
    i = len(X)
    j = len(Y)
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            st += X[i-1]
            i -= 1
            j -= 1
        else:
            if res[i][j-1] > res[i-1][j]:
                j -= 1
            else:
                i -= 1

    return ''.join(list(st)[::-1])


X = 'acbcf'
Y = 'abcdaf'
print(printLCS(X, Y, len(X), len(Y)))