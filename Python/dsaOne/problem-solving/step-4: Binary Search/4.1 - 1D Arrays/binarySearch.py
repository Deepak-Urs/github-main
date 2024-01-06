#https://leetcode.com/problems/binary-search/

def binarySearch(nums, t):
    l = 0
    r = len(nums)-1

    while l <=r:
        m = (l+r)//2

        if nums[m] == t:
            return m
        elif t < nums[m]:
            r = m - 1
        else:
            l = m + 1

    return -1

print(binarySearch([-1,0,3,5,9,12], 9))
print(binarySearch([-1,0,3,5,9,12], 2)) 
