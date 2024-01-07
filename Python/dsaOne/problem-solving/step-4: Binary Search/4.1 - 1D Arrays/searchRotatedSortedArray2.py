def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2

            if target == nums[m]:
                return True

            if nums[l] == nums[m] and nums[r] == nums[m]:
                l += 1
                r -= 1
                continue

            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False


print(search([2,5,6,0,0,1,2], 3)) 
print(search([2,5,6,0,0,1,2], 0))        