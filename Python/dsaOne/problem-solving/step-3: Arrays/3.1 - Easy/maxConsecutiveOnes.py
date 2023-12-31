#https://leetcode.com/problems/max-consecutive-ones/submissions/

def maxConsecutiveOnes(nums):
    mx = 0
    mc = 0
    for i in nums:
        if i == 1:
            mc += 1
        else:
            mx = max(mx, mc)
            mc = 0

    return max(mx, mc)


print(maxConsecutiveOnes([1,1,0,1,1,1]))
print(maxConsecutiveOnes([1,0,1,1,0,1]))