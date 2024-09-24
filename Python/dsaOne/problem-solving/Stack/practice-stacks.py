# class minimumStackImproved:
#     def __init__(self, data=[]) -> None:
#         self.stk = data
#         self.minStkVal = -1

#     def push(self, val) -> None:
#         if not len(self.stk):
#             self.stk.append(val)
#             self.minStkVal = val
#         elif self.stk[-1] <= val:
#             self.stk.append(val)
#         elif self.stk[-1] > val:
#             self.stk.append(2*val - self.minStkVal)
#             self.minStkVal = val


#     def pop(self) -> int:
#         ans = -1
#         if not len(self.stk):
#             return -1
#         elif self.stk[-1] >= self.minStkVal:
#             ans = self.stk.pop(-1)
#         elif self.stk[-1] < self.minStkVal:
#             self.minStkVal = 2*self.minStkVal - self.stk[-1]
#             self.stk.pop(-1)
#             ans = self.minStkVal
        
#         return ans

#     def getMin(self) -> int:
#         if not len(self.stk):
#             return -1
#         else:
#             return self.minStkVal
    
#     def getTop(self) -> int:
#         ans = -1
#         if not len(self.stk):
#             return -1
#         elif self.stk[-1] >= self.minStkVal:
#             ans = self.stk[-1]
#         elif self.stk[-1] < self.minStkVal:
#             ans = 2*self.minStkVal - self.stk[-1]
        
#         return ans

#     def printStacks(self) -> None:
#         print('stk -->', self.stk)


# mS = minimumStackImproved()
# # mS.printStacks()

# mS.push(18)
# # mS.printStacks()

# mS.push(19)
# mS.printStacks()
# print('minStk value', mS.getMin())

# mS.push(29)
# # mS.printStacks()

# mS.push(15)
# mS.printStacks()
# print('minStk value', mS.getMin())

# mS.push(15)
# mS.printStacks()

# mS.pop()
# # mS.printStacks()
# print('minStk value', mS.getMin())

# mS.pop()
# # mS.printStacks()
# print('minStk value', mS.getMin())




# # class minStack:
# #     def __init__(self, data=[]) -> None:
# #         self.stk = data
# #         self.minStk = []

# #     def push(self, val) -> None:
# #         self.stk.append(val)

# #         if not len(self.minStk) or self.minStk[-1] >= val:
# #             self.minStk.append(val)
        
# #         # print()
# #         return
    
# #     def pop(self) -> int:
# #         if not len(self.stk):
# #             return -1
# #         ans = self.stk.pop(-1)

# #         if ans == self.minStk[-1]:
# #             self.minStk.pop(-1)
        
# #         return ans

# #     def getMin(self) -> int:
# #         if not len(self.minStk):
# #             return -1
# #         else:
# #             return self.minStk[-1]
    
# #     def printStacks(self) -> None:
# #         print('stk -->', self.stk)
# #         print('minStk -->', self.minStk)

# # mS = minStack()
# # # mS.printStacks()

# # mS.push(18)
# # # mS.printStacks()

# # mS.push(19)
# # mS.printStacks()
# # print('minStk value', mS.getMin())

# # mS.push(29)
# # # mS.printStacks()

# # mS.push(15)
# # mS.printStacks()
# # print('minStk value', mS.getMin())

# # mS.push(15)
# # mS.printStacks()

# # mS.pop()
# # # mS.printStacks()
# # print('minStk value', mS.getMin())

# # mS.pop()
# # # mS.printStacks()
# # print('minStk value', mS.getMin())



# # # def rainWaterTrapping(nums):
# # #     l = len(nums)
# # #     mxL = [0 for _ in range(l)]
# # #     mxR = [0 for _ in range(l)]
# # #     mL = nums[0]
# # #     mR = nums[-1]
    
# # #     for i in range(l):
# # #         mxL[i] = max(mL, nums[i])
# # #         if mxL[i] > mL:
# # #             mL = mxL[i]
# # #     print('mxL', mxL)

# # #     for j in range(l):
# # #         mxR[j] = max(mR, nums[j])
# # #         if mxR[j] > mL:
# # #             mL = mxR[j]
# # #     print('mxR', mxR)
    
# # #     res = []
# # #     for k in range(l):
# # #         res.append(min(mxL[k], mxR[k]) - nums[k])
    
# # #     return sum(res)

# # # print(rainWaterTrapping([3,0,0,2,0,4]))


    


# def NSL(nums):
#     stk = []
#     res = []

#     for i in range(len(nums)):
#         if not len(stk):
#             res.append(-1)
#         elif len(stk) and stk[-1][0] < nums[i]:
#             res.append(stk[-1][1])
#         elif len(stk) and stk[-1][0] >= nums[i]:
#             while len(stk) and stk[-1][0] >= nums[i]:
#                 stk.pop(-1)
#             if not len(stk):
#                 res.append(-1)
#             else:
#                 res.append(stk[-1][1])
        
#         stk.append([nums[i], i])
    
#     return res

# def NSR(nums):
#     stk = []
#     res = []
#     l = len(nums)

#     for i in range(len(nums)-1, -1, -1):
#         if not len(stk):
#             res.append(l)
#         elif len(stk) and stk[-1][0] < nums[i]:
#             res.append(stk[-1][1])
#         elif len(stk) and stk[-1][0] >= nums[i]:
#             while len(stk) and stk[-1][0] >= nums[i]:
#                 stk.pop(-1)
#             if not len(stk):
#                 res.append(l)
#             else:
#                 res.append(stk[-1][1])
        
#         stk.append([nums[i], i])
    
#     res.reverse()
#     return res
            

# def MAH(nums):
#     nsl = NSL(nums)
#     # print(nsl)
#     nsr = NSR(nums)
#     # print(nsr)

#     width = []
#     for i in range(len(nsl)):
#         width.append(nsr[i]-nsl[i]-1)
    
#     area = []
#     for i in range(len(nums)):
#         area.append(nums[i]*width[i])
    
#     return area

# def MAHBinaryMatrix(nums):
#     mat = [0 for _ in range(len(nums[0]))]
#     nR = len(nums)
#     nC = len(nums[0])
#     areas = []


#     for i in range(nR):
#         for j in range(nC):
#             if nums[i][j] == 1:
#                 mat[j] += 1
#             else:
#                 mat[j] = 0
#         a = MAH(mat)
#         areas.append(max(a))
    
#     return max(areas)
    
# print(MAHBinaryMatrix([[0,1,1,0], [1,1,1,1], [1,1,1,1], [1,1,0,0]]))


# # print(MAH([6,2,5,4,5,1,6]))

# # # [100, 80, 60, 70, 60, 75,85]
# # def stockSpan(nums):
# #     stk = []
# #     res = []

# #     for i in range(len(nums)):
# #         if not len(stk):
# #             res.append(-1)
# #         elif len(stk) and stk[-1][0] > nums[i]:
# #             res.append(stk[-1][1])
# #         elif len(stk) and stk[-1][0] <= nums[i]:
# #             while len(stk) and stk[-1][0] <= nums[i]:
# #                 stk.pop(-1)
# #             if not len(stk):
# #                 res.append(-1)
# #             else:
# #                 res.append(stk[-1][1])
        
# #         stk.append([nums[i], i])
    
# #     print('res', res)
# #     #  indices with res
# #     for k in range(len(res)):
# #         res[k] = k-res[k]
    
# #     return res

# # print(stockSpan([100, 80, 60, 70, 60, 75,85]))


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
