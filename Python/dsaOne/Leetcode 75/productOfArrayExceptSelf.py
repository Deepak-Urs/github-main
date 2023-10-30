#https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75

def productOfArrayExceptSelf(nums):
    res = [1 for x in nums]
    prefix = 1
    postfix = 1

    for i in range(0, len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix 
        postfix *= nums[i]
    
    return res


print(productOfArrayExceptSelf([1,2,3,4]))
print(productOfArrayExceptSelf([-1,1,0,-3,3]))