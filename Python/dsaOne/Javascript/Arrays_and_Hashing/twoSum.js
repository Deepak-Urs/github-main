//https://leetcode.com/problems/two-sum/description/

const twoSum = (nums, target) => {
    var map = new Map()
    for(let i = 0; i < nums.length; i++){
        var num = nums[i]
        if (map.get(target-num) == undefined) map.set(num, i)
        else return [i, map.get(target-num)].sort()
    }
}

console.log(twoSum([1,2,3,4], 7))