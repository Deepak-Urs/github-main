# def firstOcc(nums, t, n):
#     st = 0
#     en = n - 1
#     fo = -1
    
#     while st <= en:
#         m = st + (en-st)//2
        
#         if t == nums[m]:
#             fo = m
#             en = m - 1
#         elif t < nums[m]:
#             en = m - 1
#         else:
#             st = m + 1
    
#     return fo

# def lastOcc(nums, t, n):
#     st = 0
#     en = n - 1
#     lo = -1
    
#     while st <= en:
#         m = st + (en-st)//2
        
#         if t == nums[m]:
#             lo = m
#             st = m + 1
#         elif t < nums[m]:
#             en = m - 1
#         else:
#             st = m + 1
    
#     return lo



# def firstLastOcc(nums, t):
#     n = len(nums)
#     fO = firstOcc(nums, t, n)
#     lO = lastOcc(nums, t, n)
    
#     return [fO, lO]
    
# print(firstLastOcc([1,2,3,4,4,4,5,6,7], 4))
# print(firstLastOcc([1,2,3,4,4,4,5,6,7], 6))
# print(firstLastOcc([1,2,3,4,4,4,5,6,7], 10))





# def binarySearchUnkOrd(nums, t):
#     st = 0
#     en = len(nums)-1
#     isAsc = False
    
#     if en <= 2:
#         return -1
    
#     if nums[0] <= nums[1] <= nums[2]:
#         isAsc = True
    
#     while st <= en:
#         m = st + (en-st)//2
        
#         if t == nums[m]:
#             return m
#         elif t < nums[m]:
#             if isAsc:
#                 en = m - 1
#             else:
#                 st = m + 1
#         else:
#             if isAsc:
#                 st = m + 1
#             else:
#                 en = m - 1
    
#     return -1
    

# print(binarySearchUnkOrd([9,8,7,6,5,4,3,2,1], 7))
# print(binarySearchUnkOrd([1,2,3,4,5,6,7,8,9], 5))
























# # def binarySearchDecArr(nums, t):
# #     st = 0
# #     en = len(nums)-1
    
# #     while st <= en:
# #         m = st + (en-st)//2
        
# #         if t == nums[m]:
# #             return m
# #         elif t < nums[m]:
# #             st = m + 1
# #         elif t > nums[m]:
# #             en = m - 1
    
# #     return -1
    
# # print(binarySearchDecArr([9,8,7,6,5,4,3,2,1], 7))
# # print(binarySearchDecArr([9,8,7,6,5,4,3,2,1], 15))






















# # # def binarySearch(nums, t):
# # #     st = 0
# # #     en = len(nums)-1
    
# # #     while st <= en:
# # #         m = st + (en-st)//2
        
# # #         if t == nums[m]:
# # #             return m
# # #         elif t < nums[m]:
# # #             en = m - 1
# # #         elif t > nums[m]:
# # #             st = m + 1
    
# # #     return -1
    
# # # print(binarySearch([1,2,3,4,5,6,7,8,9], 5))
# # # print(binarySearch([1,2,3,4,5,6,7,8,9], 15))