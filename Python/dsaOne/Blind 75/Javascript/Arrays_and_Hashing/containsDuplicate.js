//https://leetcode.com/problems/contains-duplicate/description/

const containsDuplicate = (nums) => {
    let hm = {}
    for (let i = 0; i < nums.length; i++) {
        if(nums[i] in hm){
            return true
        }
        else {
            hm[nums[i]] = 1
        }
    }
    return false
}

console.log(containsDuplicate([1,2,3,1]))
console.log(containsDuplicate([1,2,3,4]))