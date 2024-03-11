def printShortestCommonSubsequence(X, Y):
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
    
    st = ''
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            st += X[i-1]
            i -= 1
            j -= 1
        else:
            if res[i][j-1] > res[i-1][j]:
                st += Y[j-1]
                j -= 1
            else:
                st += X[i-1]
                i -= 1
    
    while i > 0:
        st += X[i-1]
        i -= 1

    while j > 0:
        st += Y[j-1]
        j -= 1

    return ''.join(list(st)[::-1])

print(printShortestCommonSubsequence('acbcf', 'abcdaf'))