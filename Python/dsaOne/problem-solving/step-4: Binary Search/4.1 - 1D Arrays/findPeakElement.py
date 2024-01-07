#https://leetcode.com/problems/find-peak-element/description/
def findPeakElement(nums):
    n = len(nums)

    if n == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[-2] < nums[-1]:
        return n - 1

    l = 1
    r = n-2

    while(l<=r):
        m = (l+r)//2

        if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
            return m
        
        if nums[m] > nums[m-1]:
            l = m + 1
        else:
            r = m - 1

    return -1

print(findPeakElement([1,2,3,1]))
print(findPeakElement([1,2,1,3,5,6,4]))