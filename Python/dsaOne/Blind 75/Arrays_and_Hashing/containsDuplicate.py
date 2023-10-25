#https://leetcode.com/problems/contains-duplicate/description/

def containsDuplicate(nums):
    hm = {}
    for i in nums:
        if i not in hm:
            hm[i] = 1
        else:
            return True
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([4,5,6,7]))