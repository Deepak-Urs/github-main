# def maxSubArray(nums, w):
#     i = 0
#     j = 0
#     size = len(nums)
#     q = []

#     while j < size:
#         if len(q) == 0 or nums[j] > q[0]:
#             q.append(nums[j])
#         ws = j-i+1

#         if ws < w:
#             j += 1
#         elif ws == w:
#             print(max(q))
#             if q[0] == nums[i]:
#                 q.pop(0)
            
#             j += 1
#             i += 1
    
#     return "EOP"

# print(maxSubArray([1,3,-1,-3,5,3,6,7], 3))
# print(maxSubArray([1,2,5,7,9,1,6], 3))
# print(maxSubArray([-1,-2,-3,-1,-1,-11], 3))
# print(maxSubArray([-1,-2,-3,-1,-1,-11,-6], 4))























# ("aabaabaa", "aaba")
# def countAnagramOccurances(st, t):
#     # initial ptrs
#     i = 0
#     j = 0
#     w = len(t)
#     size = len(st)
#     res = 0

#     # target str calculations
#     pO = {}
#     for v in t:
#         pO[v] = pO.get(v, 0) + 1
#     pOL = len(pO)

#     # core logic
#     while j < size:
#         if st[j] in pO:
#             pO[st[j]] -= 1

#             if pO[st[j]] == 0:
#                 pOL -= 1

#         if j-i+1 < w:
#             j += 1
#         elif j-i+1 == w:
#             if pOL == 0:
#                 res += 1
            
#             if pOL == 0 and st[i] in pO:
#                 pOL += 1
#                 pO[st[i]] += 1

#             j += 1
#             i += 1

#     return res

# print(countAnagramOccurances("aabaabaa", "aaba"))
# print(countAnagramOccurances("aabaabaa", "aba"))
# print(countAnagramOccurances("qwerty", "aba"))



# def minValSubArr(nums, w):
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
                
#             j += 1
#             i += 1
    
#     return "EOP"

# print(minValSubArr([1,2,-5,7,9,-1,6], 3))
# print(minValSubArr([-1,-2,3,1,1,-11,-6], 3))
# print(minValSubArr([-1,-2,-3,-1,12,11,6], 4))





# def maxSumSubArray(nums, w):
#     i = 0
#     j = 0
#     sm = 0
#     mx = -float('inf')
#     size = len(nums)

#     while j < size:
#         sm += nums[j]
#         ws = j-i+1

#         if ws < w:
#             j += 1
#         elif ws == w:
#             mx = max(mx, sm)
#             sm -= nums[i]

#             i += 1
#             j += 1
    
#     return mx

# print(maxSumSubArray([1,2,5,7,9,1,6], 3))
# print(maxSumSubArray([-1,-2,-3,-1,-1,-11,-6], 3))
# print(maxSumSubArray([-1,-2,-3,-1,-1,-11,-6], 4))


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

        
