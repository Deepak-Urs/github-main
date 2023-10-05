#https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    hm = {}
    for i in nums:
        if i in hm:
            return True
        else:
            hm[i] = 1
    return False
    #return len(nums) != len(set(nums))

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))