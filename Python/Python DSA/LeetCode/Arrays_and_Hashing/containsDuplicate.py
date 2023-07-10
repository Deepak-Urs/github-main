#https://leetcode.com/problems/contains-duplicate/description/

def containsDuplicate(nums):
    hm = {}
    res = False
    for i in nums:
        if i in hm:
            res = True
            break
        else:
            hm[i] = 1
    
    return res

#Example 1:
#Input: nums = [1,2,3,1]
#Output: true

#Example 2:
#Input: nums = [1,2,3,4]
#Output: false

#Example 3:
#Input: nums = [1,1,1,3,3,4,3,2,4,2]
#Output: true

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))