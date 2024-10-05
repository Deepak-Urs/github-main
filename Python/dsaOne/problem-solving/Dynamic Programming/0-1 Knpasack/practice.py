# # Z-O-KP Tabulation approach
# def z_o_kp_tabulation(Wt, Vl, W, n):
#     # initialization
#     T = [[0 if ix == 0 or jx == 0 else None for jx in range(W+1)] for ix in range(n+1)]

#     #  choice diagram
#     for i in range(1, n+1):
#         for j in range(1, W+1):
#             if Wt[i-1] <= W:
#                 T[i][j] = max((Vl[i-1] + T[i-1][j-Wt[i-1]]), T[i-1][j])
#             else:
#                 T[i][j] = T[i-1][j]
    
#     return T[i][j]


# Wt = [1,3,4,5]
# Vl = [2,4,5,7]
# W = 10
# n = len(Wt)

# print(z_o_kp_tabulation(Wt, Vl, W, n))


# Z-O-KP Memoization
# Wt = [1,3,4,5]
# Vl = [2,4,5,7]
# W = 10
# n = len(Wt)

# memo = [[] for i in range(n)]
# for j in range(n):
#     memo[j] = [-1 for i in range(W)]

# def z_o_kp_memo(Wt, Vl, W, n):
#     if W == 0 or n == 0:
#         return 0
    
#     if memo[n-1][W-1] != -1:
#         return memo[n-1][W-1]
    
#     if Wt[n-1] <= W:
#         memo[n-1][W-1] = max(Vl[n-1] + z_o_kp_memo(Wt, Vl, W- Wt[n-1], n-1), z_o_kp_memo(Wt, Vl, W, n-1))
#     elif Wt[n-1] > W:
#         memo[n-1][W-1] = z_o_kp_memo(Wt, Vl, W, n-1)

#     return memo[n-1][W-1]
    

# print(z_o_kp_memo(Wt, Vl, W, n))


## Zero One Knapsack (Basic Recursion way)
#def z_o_knapsack(Wt, Vl, W, n):
#    # v = 0

#    if W == 0 or n == 0:
#        return 0
    
#    if Wt[n-1] <= W:
#        return max((Vl[n-1] + z_o_knapsack(Wt, Vl, W-Wt[n-1], n-1)), z_o_knapsack(Wt, Vl, W, n-1) )

#    elif Wt[n-1] > W:
#        return z_o_knapsack(Wt, Vl, W, n-1)
    
#    # return v


#Wt = [1,3,4,5]
#Vl = [2,4,5,7]
#W = 10
#n = len(Wt)
#print(z_o_knapsack(Wt, Vl, W, n))