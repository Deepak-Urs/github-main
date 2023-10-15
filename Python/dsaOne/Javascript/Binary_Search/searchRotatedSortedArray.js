const searchRotatedSortedArray = (nums) => {
    let l = 0, r = nums.length-1, res = 0;

    while(l <= r){
        if(nums[l] < nums[r]) {
            res = Math.min(nums[l], res)
            break
        }

        m = Math.ceil((r+l)/2)
        res = Math.ceil(nums[m], res)
        if(nums[l] <= nums[m]) {
            l = m + 1
        } else {
            r = m - 1
        }
    }

    return res
}

console.log(searchRotatedSortedArray([3,4,5,1,2]))