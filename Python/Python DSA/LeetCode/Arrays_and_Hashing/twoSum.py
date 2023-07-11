#https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    hm = {}

    for i in range(0, len(nums)):
        another = target - nums[i]

        if another in hm:
            return sorted([i, hm[another]])
        else:
            hm[nums[i]] = i
    
    return 0

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
