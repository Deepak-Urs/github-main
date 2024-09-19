# def findFirstNegNumber(nums, w):
#     i = 0
#     j = 0
#     q = []
#     size = len(nums)

#     while j < size:
#         if nums[j] < 0:
#             q.append(nums[j])
#         ws = j-i+1

#         if ws < w:
#             j += 1
#         elif ws == w:
#             if len(q) == 0:
#                 print(0)
#             else:
#                 print(q[0])
#                 if q[0] == nums[i]:
#                     q.pop(0)
                
#             i += 1
#             j += 1
    
#     return "EOP"

# print(findFirstNegNumber([12,-1,-7,8,-15,30,16,28], 3))




# # # [2,3,5,2,9,7,1]
# # def windowSum(nums, w):
# #     mx = 0

# #     for i in range(len(nums)-w):
# #         sum = 0
# #         for j in range(i, i+w):
# #             sum += nums[j]
# #         mx = max(mx, sum)
    
# #     return mx

# # # print(windowSum([2,3,5,2,9,7,1], 3))

# # def maxSumSubarray(nums, w):
# #     i = 0
# #     j = 0
# #     size = len(nums)
# #     sm = 0
# #     mx = 0

# #     while j < size:
# #         sm += nums[j]

# #         if j-i+1 < w:
# #             j += 1
# #         elif j-i+1 == w:
# #             mx = max(sm, mx)
# #             sm -= nums[i]

# #             i += 1
# #             j += 1
    
# #     return mx

# # print(maxSumSubarray([2,3,5,2,9,8,1], 3))

        
