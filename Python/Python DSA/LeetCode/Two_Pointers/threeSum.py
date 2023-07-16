#https://leetcode.com/problems/3sum/description/

def threeSum(nums):
    res = []
    nums.sort()

    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
            
        l, r = i+1, len(nums)-1
        while l < r:
            tS = a + nums[l] + nums[r]
            if tS > 0:
                r -= 1
            elif tS < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1

    return res

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))