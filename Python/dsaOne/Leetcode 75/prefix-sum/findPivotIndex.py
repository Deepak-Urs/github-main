#https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75

def findPivotIndex(nums):
    lsum = 0
    rsum = sum(nums)

    for idx, ele in enumerate(nums):
        rsum -= ele
        
        if(lsum == rsum):
            return idx

        lsum += ele

    return -1

print(findPivotIndex([1,7,3,6,5,6]))
print(findPivotIndex([1,2,3]))
print(findPivotIndex([2,1,-1]))