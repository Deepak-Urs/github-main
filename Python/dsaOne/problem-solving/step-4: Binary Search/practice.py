#def findNextAlphabet(letters, t):
#    st = 0
#    en = len(letters)-1
#    res = -1
    
#    while st <= en:
#        m = st + (en-st)//2
        
#        if t == letters[m]:
#            st = m + 1
#        elif t < letters[m]:
#            res = m
#            en = m -1
#        else:
#            st = m + 1
    
#    return letters[res] if res != -1 else -1

#print(findNextAlphabet(['a', 'b', 'f', 'h', 'i', 'm'], 'f'))
#print(findNextAlphabet(['a', 'b', 'f', 'h', 'i', 'm'], 'i'))
#print(findNextAlphabet(['a', 'b', 'f', 'h', 'i', 'm'], 'm'))
#print(findNextAlphabet(['a', 'b', 'f', 'h', 'i', 'm'], 'q'))


## def ceilValue(nums, t):
##     st = 0
##     en = len(nums)-1
##     res = -1
    
##     while st <= en:
##         m = st + (en-st)//2
        
##         if t == nums[m]:
##             return nums[m]
##         elif t < nums[m]:
##             res = m
##             en = m - 1
##         else:
##             st = m + 1
    
##     return nums[res] if res != -1 else -1

## print(ceilValue([1,2,3,4,8,10,12,19], 5))
## print(ceilValue([1,2,3,4,8,10,12,19], 9))
## print(ceilValue([1,2,3,4,8,10,12,19], 19))
## print(ceilValue([1,2,3,4,8,10,12,19], 219))
## print(ceilValue([1,2,3,4,8,10,12,19], 0))

## def floorVal(nums, t):
##     st = 0
##     en = len(nums)-1
##     res = -1
    
##     while st <= en:
##         m = st + (en-st)//2
        
##         if t == nums[m]:
##             return nums[m]
##         if t < nums[m]:
##             en = m - 1
##         else:
##             res = m
##             st = m + 1
    
##     return nums[res] if res != -1 else -1

## print(floorVal([1,2,3,4,8,10,12,19], 5))
## print(floorVal([1,2,3,4,8,10,12,19], 9))
## print(floorVal([1,2,3,4,8,10,12,19], 19))
## print(floorVal([1,2,3,4,8,10,12,19], 219))
## print(floorVal([1,2,3,4,8,10,12,19], 0))


## def binSrchNearSortArr(nums, t):
##     st = 0
##     en = len(nums)-1
    
##     while st <= en:
##         m = st + (en-st)//2
        
##         if t == nums[m]:
##             return m
##         elif st <= m-1 and t == nums[m-1]:
##             return m-1
##         elif m+1 <= en and t == nums[m+1]:
##             return m+1
##         elif t < nums[m]:
##             en = m - 1
##         else:
##             st = m + 1
    
##     return -1
    
## print(binSrchNearSortArr([10,20,30,50,40], 50))
## print(binSrchNearSortArr([10,20,30,50,40], 60))
## print(binSrchNearSortArr([10,20,30,50,40], 20))

# helper fn-1
def numTimesArrRotated(nums):
    l = len(nums)
    st = 0
    en = l - 1
    
    while st <= en:
        m = st + (en-st)//2
        
        prev = (m+l-1)%l
        nxt = (m+1)%l
        
        if nums[m] <= nums[prev] and nums[m] <= nums[nxt]:
            return m
        elif nums[m] >= nums[en]:
            st = m + 1
        else:
            en = m - 1
    
    return -1
    
# helper fn-2
# def binSrch(nums, t, st, en):
#     while st <= en:
#         m = st + (en-st)//2
        
#         if t == nums[m]:
#             return m
#         elif t < nums[m]:
#             en = m - 1
#         else:
#             st = m + 1
    
#     return -1
            
# #  to be fixed
# def findEleInRotArr(nums, t):
#     minValIdx = numTimesArrRotated(nums)
#     print('minValIdx=', minValIdx)
#     l = nums
#     r1 = -1
#     r2 = -1
    
#     if minValIdx == 0:
#         st = 0
#         en = l - 1
#         res = binSrch(nums, t, st, en)
#         return res
#     else:
#         # if t >= nums[0] and t <= nums[minValIdx-1]:
#         r1 = binSrch(nums, t, 0, minValIdx-1)
#         print('r1=', r1)
#         if r1 == -1:
            
#         # elif t >= nums[minValIdx-1] and t <= nums[l-1]:
#             r2 = binSrch(nums, t, minValIdx, l-1)
    
#     if r1 == -1 and r2 == -1:
#         return -1
#     elif r1 == -1:
#         return r2
#     else:
#         return r1
        
    
# print(findEleInRotArr([11,12,15,18,2,5,6,8], 15))
# print(findEleInRotArr([11,12,15,18,2,5,6,8], 35))
# # print(findEleInRotArr([2,5,6,8,11,12,15,18], 12))
            

# # def numTimesArrRotated(nums):
# #     l = len(nums)
# #     st = 0
# #     en = l - 1
    
# #     while st <= en:
# #         m = st + (en-st)//2
        
# #         prev = (m+l-1)%l
# #         nxt = (m+1)%l
        
# #         if nums[m] <= nums[prev] and nums[m] <= nums[nxt]:
# #             return m
# #         elif nums[m] >= nums[en]:
# #             st = m + 1
# #         else:
# #             en = m - 1
    
# #     return -1
    
# # print(numTimesArrRotated([11,12,15,18,2,5,6,8]))
# # print(numTimesArrRotated([2,5,6,8,11,12,15,18]))



# # def firstOcc(nums, t, n):
# #     st = 0
# #     en = n
# #     res = -1
    
# #     while st <= en:
# #         m = st + (en-st)//2
        
# #         if t == nums[m]:
# #             res = m
# #             en = m - 1
# #         elif t < nums[m]:
# #             en = m - 1
# #         else:
# #             st = m + 1
    
# #     return res

# # def lastOcc(nums, t, n):
# #     st = 0
# #     en = n
# #     res = -1
    
# #     while st <= en:
# #         m = st + (en-st)//2
        
# #         if t == nums[m]:
# #             res = m
# #             st = m + 1
# #         elif t < nums[m]:
# #             en = m - 1
# #         else:
# #             st = m + 1
    
# #     return res

# # def countEle(nums, t):
# #     n = len(nums)-1
# #     si = firstOcc(nums, t, n)
# #     li = lastOcc(nums, t, n)
    
# #     return li-si+1 if li != -1 and si != -1 else -1
    

# # print(countEle([2,4,10,10,10,18,20], 10))
# # print(countEle([2,4,10,10,10,18,20], 4))
# # print(countEle([2,4,10,10,10,18,20], 14))


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