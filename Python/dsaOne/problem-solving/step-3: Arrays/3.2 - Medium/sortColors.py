#https://leetcode.com/problems/sort-colors/

def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    z = 0
    o = 0
    t = 0

    for i in nums:
        if i == 0:
            z += 1
        elif i == 1:
            o += 1
        else:
            t += 1

    for i in range(z):
        nums[i] = 0
    
    for i in range(z, z+o):
        nums[i] = 1

    for i in range(z+o, z+o+t):
        nums[i] = 2

    return nums

print(sortColors([2,0,2,1,1,0]))
print(sortColors([2,0,1]))