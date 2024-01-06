#https://leetcode.com/problems/search-insert-position/description/


def searchInsertPosition(nums, t):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l+r)//2

        if nums[m] == t:
            return m
        elif t < nums[m]:
            r = m - 1
        else:
            l = m + 1
    
    return l

print(searchInsertPosition([1,3,5,6], 5))
print(searchInsertPosition([1,3,5,6],2))
print(searchInsertPosition([1,3,5,6],7))
print(searchInsertPosition([1,3,5,6],4))