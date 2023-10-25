const threeSum = function(nums) {
    nums.sort((a,b) => a - b)
    let res = []
    
    for(let i = 0; i < nums.length; i++) {
        let l = i+1
        let r = nums.length - 1
        let sum = 0

        while(l < r) {
            sum = nums[i] + nums[l] + nums[r]
            if(sum == 0) {
                res.push([nums[i], nums[l], nums[r]])
                while(nums[l] == nums[l+1]) l++
                while(nums[r] == nums[r-1]) r--
                l++;
                r--;
            }
            else if(sum < 0) {
                l++;
            }
            else if(sum > 0) {
                r--;
            }
        }
        while(nums[i+1] === nums[i]) i++
    }

    return res
};

console.log(threeSum([-1,0,1,2,-1,-4]))