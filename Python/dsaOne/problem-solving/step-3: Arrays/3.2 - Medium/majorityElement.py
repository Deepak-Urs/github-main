#https://leetcode.com/problems/majority-element/description/

def majorityElement(nums):
    hm = {}
    for i in nums:
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 1
    
    mv = 0
    l = len(nums)/2
    for i in hm:
        if hm[i] > l:
            mv = i

    return mv
            
print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
    