#https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75

def diffTwoArrays(nums1, nums2):
    return [set(nums1)-set(nums2), set(nums2)-set(nums1)]

print(diffTwoArrays([1,2,3], [2,4,6]))
print(diffTwoArrays([1,2,3,3], [1,1,2,2]))