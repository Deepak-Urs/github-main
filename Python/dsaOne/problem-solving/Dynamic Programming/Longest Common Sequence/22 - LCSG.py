def longestCommonSubstring(X, Y):
    r = len(X) + 1
    c = len(Y) + 1
    res = [[] for _ in range(r)]
    mx = 0

    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0: res[i].append(0)
            else: res[i].append(None)
    
    for i in range(1,r):
        for j in range(1,c):
            if X[i-1] == Y[j-1]:
                res[i][j] = 1 + res[i-1][j-1]
                mx = max(mx, res[i][j])
            elif X[i-1] != Y[j-1]:
                res[i][j] = 0
    
    #for i in range(r):
    #    print(res[i])
    return mx


X = 'abcdtf'
Y = 'abcdep'
print(longestCommonSubstring(X, Y))