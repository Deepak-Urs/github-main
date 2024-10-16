# def printLCS(X, Y, m, n):
#     r = m + 1
#     c = n + 1
#     res = [[] for _ in range(r)]
#     #mx = 0
#     st = ''
#     #isC = False
#     #stR = []

#     for i in range(r):
#         for j in range(c):
#             if i == 0 or j == 0: res[i].append(0)
#             else: res[i].append(None)
    
#     for i in range(1,r):
#         for j in range(1,c):
#             if X[i-1] == Y[j-1]:
#                 res[i][j] = 1 + res[i-1][j-1]
#             elif X[i-1] != Y[j-1]:
#                 res[i][j] = max(res[i-1][j], res[i][j-1])
    
#     i = len(X)
#     j = len(Y)
#     while i > 0 and j > 0:
#         if X[i-1] == Y[j-1]:
#             st += X[i-1]
#             i -= 1
#             j -= 1
#         else:
#             if res[i][j-1] > res[i-1][j]:
#                 j -= 1
#             else:
#                 i -= 1

#     return ''.join(list(st)[::-1])


# X = 'acbcf'
# Y = 'abcdaf'
# print(printLCS(X, Y, len(X), len(Y)))


# def LCS(X, Y, m, n):
#     # computation
#     for i in range(1, m):
#         for j in range(1, n):
#             if X[i-1] == Y[j-1]:
#                 T[i][j] = 1 + T[i-1][j-1]
#             elif X[i-1] != Y[j-1]:
#                 T[i][j] = max(T[i-1][j], T[i][j-1])
#     print(T[i][j])
#     return T


# def printLCS(T, X, Y, m, n):
#     # tracing
#     print('input T', T)
#     iv = m
#     jv = n
#     res = ""
#     while iv > 0 and jv > 0:
#         if X[iv-1] == Y[jv-1]:
#             res += X[iv-1]
#             iv -= 1
#             jv -= 1
#         else:
#             if T[iv-1][jv] > T[iv][jv-1]:
#                 iv -= 1
#             else:
#                 jv -= 1
#     print(res)
#     # return "".join(reversed(list(res)))

# X = "abcde"
# Y = "abcj"
# m = len(X)
# n = len(Y)

# # initialization
# T = [[] for _ in range(m+1)]
# for ix in range(m+1):
#     for jx in range(n+1):
#         if ix == 0 or jx == 0:
#             T[ix].append(0)
#         else:
#             T[ix].append(None)


# res = LCS(X, Y, m, n)
# print(printLCS(res, X, Y, m, n))






# def longestCommonSubstring(X, Y, m, n):
#     mx = 0
#     T = [[] for _ in range(m+1)]
#     for ix in range(m+1):
#         for jx in range(n+1):
#             if ix == 0 or jx == 0:
#                 T[ix].append(0)
#             else:
#                 T[ix].append(None)

#     for i in range(1, m):
#         for j in range(1, n):
#             if X[i-1] == Y[j-1]:
#                 T[i][j] = 1 + T[i-1][j-1]
#                 mx = max(mx, T[i][j])
#             elif X[i-1] != Y[j-1]:
#                 T[i][j] = 0
    
#     return mx

# X = "abcde"
# Y = "abcj"
# m = len(X)
# n = len(Y)

# print(longestCommonSubstring(X, Y, m, n))

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