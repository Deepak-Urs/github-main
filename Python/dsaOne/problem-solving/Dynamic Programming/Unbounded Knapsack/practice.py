# def minNumCoins(coins, change):
#     r = len(coins)+1
#     c = change+1

#     T = [[] for _ in range(r)]
#     for ix in range(r):
#         for jx in range(c):
#             if ix == 0 and jx == 0:
#                 T[ix].append(float('inf')-1)
#             elif ix == 0:
#                 T[ix].append(float('inf')-1)
#             elif jx == 0:
#                 T[ix].append(0)
#             else:
#                 T[ix].append(None)
    
#     for sj in range(1, len(T[1])):
#         if sj % coins[0] == 0:
#             T[1][sj] = int(sj//coins[0])
#         else:
#             T[1][sj] = float('inf')

#     for i in range(1, r):
#         for j in range(1, c):
#             if coins[i-1] <= j:
#                 T[i][j] = min(T[i-1][j], 1+T[i][j-coins[i-1]])
#             elif coins[i-1] > j:
#                 T[i][j] = T[i-1][j]
    
#     return T[i][j]

# print(minNumCoins([1,2,3,4], 5))

    



            


# # def coinChangeUB(coins, change):
# #     r = len(coins)+1
# #     c = change+1

# #     T = [[] for _ in range(r)]
# #     for ix in range(r):
# #         for jx in range(c):
# #             if ix == 0 and jx == 0:
# #                 T[ix].append(1)
# #             elif ix == 0:
# #                 T[ix].append(0)
# #             elif jx == 0:
# #                 T[ix].append(1)
# #             else:
# #                 T[ix].append(None)
    
# #     for i in range(1, r):
# #         for j in range(1, c):
# #             if coins[i-1] <= j:
# #                 T[i][j] = T[i-1][j] + T[i][j-coins[i-1]]
# #             elif coins[i-1] > j:
# #                 T[i][j] = T[i-1][j]

# #     return T[i][j]

# # print(coinChangeUB([1,2,3], 5)) 
# # print(coinChangeUB([1,2,3], 6)) 




# def rodCutting(Ln, Pr, L, n):
#     r = n+1
#     c = len(Ln)+1

#     T = [[] for _ in range(r)]
#     for ix in range(r):
#         for jx in range(c):
#             if ix == 0 or jx == 0:
#                 T[ix].append(0)
#             else:
#                 T[ix].append(None)
    
#     for i in range(1, r):
#         for j in range(1, c):
#             if Ln[i-1] <= j:
#                 T[i][j] = max(Pr[i-1] + T[i][j-Ln[i-1]], T[i-1][j])
#             else:
#                 T[i][j] = T[i-1][j]

#     return T[i][j]

# Ln = [1,3,4,5]
# Pr = [2,4,5,7]
# L = 10
# n = len(Ln)

# print(rodCutting(Ln, Pr, L, n))

# # Wt = [1,3,4,5]
# # Vl = [2,4,5,7]
# # W = 10
# # n = len(Wt)

# # t = [[0 if ix ==0 or jx ==0 else None for jx in range(W+1)] for ix in range(n+1)]
# # #prints(t)

# # def unboundedKpTabulation(Wt, Vl, W, n):
# #     for i in range(1,n+1):
# #         for j in range(1, W+1):
# #             if Wt[i-1] <= j:
# #                 t[i][j] = max(Vl[i-1] + t[i][j-Wt[i-1]], t[i-1][j])
# #             else:
# #                 t[i][j] = t[i-1][j]

# #     # print(t)
# #     return t[i][j]
    
    

# # print(unboundedKpTabulation(Wt, Vl, W, n))

