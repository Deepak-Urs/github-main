def searchSingleElement(nums):
    if len(nums) == 1 or nums[0] != nums[1]:
        return nums[0]
    elif nums[-2] != nums[-1]:
        return nums[-1]

    l = 0
    r = len(nums)-1

    while l <=r:
        m = (l+r)//2

        if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
            return nums[m]
        
        if (m%2 == 0 and nums[m] == nums[m+1]) or (m%2 == 1 and nums[m] == nums[m-1]):
            l = m + 1
        else:
            r = m - 1
        
    return -1

print(searchSingleElement([1,1,2,3,3,4,4,8,8]))
print(searchSingleElement([3,3,7,7,10,11,11]))