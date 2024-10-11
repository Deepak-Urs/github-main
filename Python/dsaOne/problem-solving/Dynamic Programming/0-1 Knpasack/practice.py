#def count_subset_sum_diff(nums, sm):
#     #  initialization
#     r = len(nums)+1
#     c = sm+1
#     T = [[] for _ in range(r)]
#     for ix in range(r):
#         for jx in range(c):
#             if ix == 0 and jx == 0:
#                 T[ix].append(1)
#             elif ix == 0:
#                 T[ix].append(0)
#             elif jx == 0:
#                 T[ix].append(1)
#             else:
#                 T[ix].append(None)

#     #  computation
#     for i in range(1, r):
#         for j in range(1, c):
#             if nums[i-1] <= sm:
#                 T[i][j] = T[i-1][j-nums[i-1]] + T[i-1][j]
#             elif nums[i-1] > sm:
#                 T[i][j] = T[i-1][j]
    
#     return T[i][j]



# def count_num_subset_diff(nums, diff):
#     sm = (diff + len(nums)) // 2
#     return count_subset_sum_diff(nums, sm)

# print(count_num_subset_diff([1,1,2,3], 1)) #2
# print(count_num_subset_diff([1,2,3,4,5], 1)) #2



#def subset_sum(arr, rng):
#     r = len(arr)+1
#     c = rng+1
#     T = [[] for _ in range(r)]

#     for ix in range(r):
#         for jx in range(c):
#             if ix == 0 and jx == 0:
#                 T[ix].append(True)
#             elif ix == 0:
#                 T[ix].append(False)
#             elif jx == 0:
#                 T[ix].append(True)
#             else:
#                 T[ix].append(None)

    
#     for i in range(1, r):
#         for j in range(1, c):
#             if arr[i-1] <= j:
#                 T[i][j] = T[i-1][j-arr[i-1]] or T[i-1][j]
#             elif arr[i-1] > j:
#                 T[i][j] = T[i-1][j]
    
#     return T

# def zokp_min_difference_subset_sum(nums):
#     rng = sum(nums)
#     res = subset_sum(nums, rng)

#     subset_sum_range = []
#     for jx in range(len(res[0])//2):
#         if jx == True:
#             subset_sum_range.append(jx)
    
#     mn = float('inf')
#     for i in subset_sum_range:
#         mn = min(mn, rng-(2*i))
    
#     return mn



# print(zokp_min_difference_subset_sum([1,2,7])) 

# # print(zokp_min_difference_subset_sum([1,2,3,5,6,8,10], 11)) 






# # def zokp_count_subset_sum(arr, sm):
# #     r = len(arr)+1
# #     c = sm+1
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
# #             if arr[i-1] <= j:
# #                 T[i][j] = T[i-1][j-arr[i-1]] + T[i-1][j]
# #             elif arr[i-1] > j:
# #                 T[i][j] = T[i-1][j]
    
# #     return T[i][j]

# # print(zokp_count_subset_sum([2,3,5,6,8,10], 10)) 
# # # 2,3,5; 2,8; 10

# # print(zokp_count_subset_sum([1,2,3,5,6,8,10], 11)) 
# # # 1,2,3,5; 2,3,6; 3,8; 1,10; 5,6; 2,3,6



#class SS:
#    def __init__(self, arr=[]) -> None:
#        self.arr = arr
    
#    def subset_sum(self, arr, sm):
#        r = len(arr)+1
#        c = sm+1

#        T = [[] for _ in range(r)]
#        for ix in range(r):
#            for jx in range(c):
#                if ix == 0:
#                    T[ix].append(False)
#                elif jx == 0:
#                    T[ix].append(True)
#                else:
#                    T[ix].append(None)
#        # print(T)
        
#        for i in range(r):
#            for j in range(c):
#                if arr[i-1] <= j:
#                    T[i][j] = T[i-1][j-arr[i-1]] or T[i-1][j]
#                elif arr[i-1] > j:
#                    T[i][j] = T[i-1][j]
        
#        return T[i][j]


#    def equal_sum_partition(self):
#        sm = sum(self.arr)
#        if sm % 2 != 0:
#            return False
#        return self.subset_sum(self.arr, sm//2)


## ESS = SS([1,5,11,5])
#ESS = SS([2,5,7,6,10])
#print(ESS.equal_sum_partition())


    



#def zokp_subset_sum(arr, sm):
#     # initialization
#     r = len(arr)+1
#     c = sm+1
#     res = [[] for ix in range(r)]
#     for i in range(len(res)):
#         for j in range(c):
#             if i == 0 and j == 0: res[i].append(True)
#             elif j == 0: res[i].append(True)
#             elif i == 0: res[i].append(False)
#             else: res[i].append(None)

#     # finding result
#     for i in range(1, r):
#         for j in range(1, c):
#             if arr[i-1] <= j:
#                 res[i][j] = res[i-1][j-arr[i-1]] or res[i-1][j]
#             elif arr[i-1] > j:
#                 res[i][j] = res[i-1][j]

#     #for ix in res:
#     #    print(ix)

#     return res[i][j]


# print(zokp_subset_sum([2,3,7,8,10], 12))


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