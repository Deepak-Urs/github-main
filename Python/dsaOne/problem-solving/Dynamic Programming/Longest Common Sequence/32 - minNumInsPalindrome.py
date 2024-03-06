def minNumInsPalindrome(X):
    Y = ''.join(list(X)[::-1])
    r = len(X) + 1
    c = len(Y) + 1
    res= [[] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0: res[i].append(0)
            else: res[i].append(None)
    
    for i in range(1, r):
        for j in range(1, c):
            if X[i-1] == Y[j-1]:
                res[i][j] = 1 + res[i-1][j-1]
            else:
                res[i][j] = max(res[i][j-1], res[i-1][j])
    
    return r - 1 - res[i][j]

print(minNumInsPalindrome('aebcbda'))