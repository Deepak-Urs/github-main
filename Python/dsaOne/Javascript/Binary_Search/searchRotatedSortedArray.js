//https://leetcode.com/problems/search-in-rotated-sorted-array/description/

const searchRotatedSortedArray = (nums, target) => {
    let l = 0, r = nums.length - 1

    while(l <= r){
        m = Math.ceil((l+r)/2)
        if(nums[m] == target) {
            return m
        }

        if(nums[l] <= nums[m]) {
            if(target < nums[l] || target > nums[m]) {
                l = m + 1
            }
            else {
                r = m - 1
            }
        }
        else {
            if(target < nums[m] || target > nums[r]) {
                r = m - 1
            }
            else {
                l = m + 1
            }
        }
    }

    return -1

}

console.log(searchRotatedSortedArray([4,5,6,7,0,1,2], 0))