#https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    hm = {}

    for i in range(0, len(nums)):
        another = target - nums[i]

        if another not in hm:
            hm[nums[i]] = i
        else:
            return sorted([i, hm[another]])

    return []
    
print(twoSum([2,7,12,17], 9))
print(twoSum([2,7,12,17], 10))