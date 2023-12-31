#https://leetcode.com/problems/move-zeroes/
def moveAllZerosToEndOfArray(nums):
    l  = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
    
    return nums

print(moveAllZerosToEndOfArray([1,2,0,4,7,0,6]))
print(moveAllZerosToEndOfArray([0,0,2,4,6]))