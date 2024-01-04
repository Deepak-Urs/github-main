#https://leetcode.com/problems/rearrange-array-elements-by-sign/description/


def rearrangeArray(nums):
    p = []
    n = []

    for i in nums:
        if i > 0:
            p.append(i)
        else:
            n.append(i)
    
    l = 0
    r = 0

    i = 0
    while l < len(p):
        nums[i] = p[l]
        l += 1
        nums[i+1] = n[r]
        r += 1

        i += 2

    return nums

print(rearrangeArray([3,1,-2,-5,2,-4]))
print(rearrangeArray([-1,1]))