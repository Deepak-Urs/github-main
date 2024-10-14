# def lcsTabulation(X, Y):
#     r = len(X)+1
#     c = len(Y)+1

#     T = [[] for i in range(r)]
#     for ix in range(r):
#         for jx in range(c):
#             if ix == 0 or jx == 0:
#                 T[ix].append(0)
#             else:
#                 T[ix].append(None)
    
#     for i in range(1, r):
#         for j in range(1, c):
#             if X[i-1] == Y[j-1]:
#                 T[i][j] = 1 + T[i-1][j-1]
#             elif X[i-1] != Y[j-1]:
#                 T[i][j] = max(T[i][j-1], T[i-1][j])
    
#     return T[i][j]

# X = 'abcdefgh'
# Y = 'abedcgl'
# print(lcsTabulation(X, Y))

# def lcsMemo(X, Y, m, n):
#     if n == 0 or m == 0:
#         return 0

#     if memo[m-1][n-1] != -1:
#         return memo[m-1][n-1]

#     if X[m-1] == Y[n-1]:
#         memo[m-1][n-1] = 1 + lcsMemo(X, Y, m-1, n-1)
#     elif X[m-1] != Y[n-1]:
#         memo[m-1][n-1] = max(lcsMemo(X, Y, m, n-1), lcsMemo(X, Y, m-1, n))
    
#     return memo[m-1][n-1]


# X = 'abcdefgh'
# Y = 'abedcgl'
# m = len(X)
# n = len(Y)
# memo = [[] for i in range(m)]
# for i in range(m):
#     memo[i] = [-1 for j in range(n)]


# print(lcsMemo(X, Y, m, n))


# def longestCommonSubsequence(x, y, n, m):
#     if n == 0 or m == 0:
#         return 0
    
#     if x[n-1] == y[m-1]:
#         return 1 + longestCommonSubsequence(x, y, n-1, m-1)
#     elif x[n-1] != y[m-1]:
#         return max(longestCommonSubsequence(x, y, n, m-1), longestCommonSubsequence(x, y, n-1, m))

# a = 'abcdefgh'
# b = 'abedcgl'
# print(longestCommonSubsequence(a, b, len(a)-1, len(b)-1))