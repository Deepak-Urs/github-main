# def searchIn2DArraySorted(nums, t):
#     # iRn * jCm
#     n = len(nums)
#     m = len(nums[0])
#     i = 0
#     j = m-1
    
#     while i >= 0 and i < n and j >= 0 and j < m:
#         if nums[i][j] == t:
#             return [i,j]
#         elif t > nums[i][j]:
#             i += 1
#         elif t < nums[i][j]:
#             j -= 1
    
#     return -1
    
# print(searchIn2DArraySorted([[10,20,30,40], [15,25,35,45], [27,29,37,45],[32,33,39,59]],29))


# def maxEleBitonicArrIdx(nums):
#     n = len(nums)
#     st = 0
#     en = n-1
    
#     while st <= en:
#         m = st + (en-st)//2
        
#         if st <= n-1 and en >= 0:
#             if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
#                 return m
#             elif nums[m] > nums[m-1]:
#                 st = m + 1
#             else:
#                 en = m - 1
#         elif m == 0:
#             return m if nums[m] > nums[m+1] else nums[m+1]
#         elif m == n-1:
#             return m if nums[m] > nums[m-1] else nums[m-1]
    
#     return -1

# def binSearch(nums, st, en, t, isAsc):
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
    
# # print(maxEleBitonicArr([5,10,20,15]))
# # print(maxEleBitonicArr([5,10,20,25,17,11,4]))
# # print(maxEleBitonicArr([15,15,15,15]))

# def searchValInBitonicArr(nums, t):
#     n = len(nums)
#     peakEleIdx = maxEleBitonicArrIdx(nums)
#     res = -1
#     # print('peakEleIdx-', peakEleIdx)
    
#     if peakEleIdx != -1:
#         if t == nums[peakEleIdx]:
#             return peakEleIdx
#         else:
#             r1 = binSearch(nums, 0, peakEleIdx, t, True)
#             # print('r1-', r1)
#             r2 = binSearch(nums, peakEleIdx+1, n-1, t, False)
#             # print('r2-', r2)
    
#         if r1 == -1 and r2 == -1:
#             return -1
#         elif r1 == -1:
#             return r2
#         else:
#             return r1
    
#     else:
#         return 0 if nums[0] == t else -1
    
# print(searchValInBitonicArr([5,10,20,15], 10))
# print(searchValInBitonicArr([5,10,20,25,17,11,4], 17))
# print(searchValInBitonicArr([15,15,15,15], 16))















# # def maxEleBitonicArr(nums):
# #     n = len(nums)
# #     st = 0
# #     en = n-1
    
# #     while st <= en:
# #         m = st + (en-st)//2
        
# #         if st <= n-1 and en >= 0:
# #             if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
# #                 return nums[m]
# #             elif nums[m] > nums[m-1]:
# #                 st = m + 1
# #             else:
# #                 en = m - 1
# #         elif m == 0:
# #             return nums[m] if nums[m] > nums[m+1] else nums[m+1]
# #         elif m == n-1:
# #             return nums[m] if nums[m] > nums[m-1] else nums[m-1]
    
# #     return -1
    
# # print(maxEleBitonicArr([5,10,20,15]))
# # print(maxEleBitonicArr([5,10,20,25,17,11,4]))
# # print(maxEleBitonicArr([15,15,15,15]))








# # def findPeakEle(arr):
# #     n = len(arr)
# #     st = 0
# #     en = n-1
    
# #     while st <= en:
# #         m = st + (en-st)//2
        
# #         if st <= n-1 and en >= 0:
# #             if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
# #                 return arr[m]
# #             elif arr[m] > arr[m-1]:
# #                 st = m + 1
# #             else:
# #                 en = m - 1
# #         elif m == 0:
# #             return arr[m] if arr[m] > arr[m+1] else arr[m+1]
# #         elif m == n-1:
# #             return arr[m] if arr[m] > arr[m-1] else arr[m-1]
            
# # print(findPeakEle([5,10,20,15]))
# # print(findPeakEle([5,10,20,25,17,11,4]))
# # print(findPeakEle([15,15,15,15]))
        


## [5,10,20,15]
#def findPeakEle(nums):
#    st = 0
#    en = len(nums)-1
    
#    while st <= en:
#        m = st + (en-st)//2
        
#        if m > 0 and m < len(nums)-1:
#            if nums[m] >= nums[m-1] and nums[m] >= nums[m+1]:
#                return nums[m]
#            elif nums[m] > nums[m-1]:
#                st = m + 1
#            else:
#                en = m - 1
#        elif m == 0:
#            return nums[m] if nums[m] > nums[m+1] else nums[m+1]
#        elif m == len(nums)-1:
#            return nums[m] if nums[m] > nums[m-1] else nums[m-1]
    
#    return -1
    
#print(findPeakEle([5,10,20,15]))
#print(findPeakEle([1,1,1,1]))
#print(findPeakEle([1000,10,100,101]))
#print(findPeakEle([1,10,1000,1010]))