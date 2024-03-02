def LCSMemo(X, Y, m, n):
    if m == 0 or n == 0: return 0

    if res[m-1][n-1] != -1: return res[m-1][n-1]

    if X[m-1] == Y[n-1]:
        res[m-1][n-1] = 1 + LCSMemo(X, Y, m-1, n-1)
    elif X[m-1] != Y[n-1]:
        res[m-1][n-1] = max(LCSMemo(X, Y, m-1, n), LCSMemo(X, Y, m, n-1))

    
    return res[m-1][n-1]


X = 'AXYT'
Y = 'AZYU'
m = len(X)
n = len(Y)
res = [[] for i in range(m)]
for i in range(m):
    res[i] = [-1 for j in range(n)]
 
print(LCSMemo(X, Y, m, n))