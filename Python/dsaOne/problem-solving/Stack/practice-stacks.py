# # Nearest Smallest-element to Left / Previous Smaller Element
# # print(NSL([1,3,2,4])) --> -1, 1, 1, 2
# # print(NSL([1,0,0,2,7,5,4]))
# # print(NSL([-1,-3,-2,-4]))
# def NSL(nums):
#     stk = []
#     res = []

#     for i in range(len(nums)):
#         if not len(stk):
#             res.append(None)
#         elif len(stk) and stk[-1] < nums[i]:
#             res.append(stk[-1])
#         elif len(stk) and stk[-1] >= nums[i]:
#             while len(stk) and stk[-1] >= nums[i]:
#                 stk.pop(-1)
#             if not len(stk):
#                 res.append(None)
#             else:
#                 res.append(stk[-1])

#         stk.append(nums[i])
    
#     return res

# print(NSL([1,3,2,4])) # --> -1, 1, 1, 2
# print(NSL([1,0,0,2,7,5,4]))
# print(NSL([-1,-3,-2,-4]))




# # Nearest Greater-element to Left / Previous Greater Element
# # print(NGL([1,3,2,4])) --> -1, -1, 3, -1
# # print(NGL([1,0,0,2,7,5,4]))
# # print(NGL([-1,-3,-2,-4]))

# # def NGL(nums):
# #     stk = []
# #     res = [] 

# #     for i in range(len(nums)):
# #         if not len(stk):
# #             res.append(None)
# #         elif len(stk) and stk[-1] > nums[i]:
# #             res.append(stk[-1])
# #         elif len(stk) and stk[-1] <= nums[i]:
# #             while len(stk) and stk[-1] <= nums[i]:
# #                 stk.pop(-1)
# #             if not len(stk):
# #                 res.append(None)
# #             else:
# #                 res.append(stk[-1])
        
# #         stk.append(nums[i])
    
# #     return res

# # print(NGL([1,3,2,4])) # --> -1, -1, 3, -1
# # print(NGL([1,0,0,2,7,5,4]))
# # print(NGL([-1,-3,-2,-4]))




# # Next Smaller-element to Right / Next Smallest Element
# # def NSR(nums):
# #     stk = []
# #     res = []

# #     for i in range(len(nums)-1,-1,-1):
# #         if not len(stk):
# #             res.append(None)
# #         elif len(stk) and stk[-1] < nums[i]:
# #             res.append(stk[-1])
# #         elif len(stk) and stk[-1] >= nums[i]:
# #             while len(stk) and stk[-1] >= nums[i]:
# #                 stk.pop(-1)
# #             if not len(stk):
# #                 res.append(None)
# #             else:
# #                 res.append(stk[-1])
        
# #         stk.append(nums[i])
    
# #     res.reverse()
# #     return res
            
# # print(NSR([1,3,2,4]))
# # print(NSR([1,0,0,2,7,5,4]))
# # print(NSR([-1,-3,-2,-4]))

# # # Next Greater-element to Right / Next Largest Element
# # def NGR(nums):
# #     stk = []
# #     res = []

# #     for i in range(len(nums)-1, -1, -1):
# #         if not len(stk):
# #             res.append(None)
# #         elif len(stk) and stk[-1] > nums[i]:
# #             res.append(stk[-1])
# #         elif len(stk) and stk[-1] <= nums[i]:
# #             while len(stk) and stk[-1] <= nums[i]:
# #                 stk.pop(-1)
# #             if not len(stk):
# #                 res.append(None)
# #             else:
# #                 res.append(stk[-1])
        
# #         stk.append(nums[i])
    
# #     res.reverse()
# #     return res

# # print(NGR([1,3,2,4]))
# # print(NGR([1,0,0,2,7,5,4]))
# # print(NGR([-1,-3,-2,-4]))


# # Next Greater-element to Right / Next Largest Element
# # [1,3,2,4]
# # def ngr(nums):
# #     res = []
# #     l = len(nums)

# #     for i in range(l-1):
# #         for j in range(i+1, l):
# #             if nums[j] > nums[i]:
# #                 print(nums[j])
# #                 break
# #             else:
# #                 print(-1)
    
# #     # return res

# # print(ngr([1,3,2,4])) --> 3,4,4,-1
