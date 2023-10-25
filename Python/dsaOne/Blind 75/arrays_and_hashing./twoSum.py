#https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    hm = {}
    for i in range(len(nums)):
        another = target - nums[i]
        if another in hm:
            return [i, hm[another]]
        else:
            hm[nums[i]] = i
    return []

print(twoSum([2,4,6,1], 10))
print(twoSum([2,4,6,1], 17))
