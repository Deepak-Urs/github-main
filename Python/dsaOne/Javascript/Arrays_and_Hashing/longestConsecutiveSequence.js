//https://leetcode.com/problems/longest-consecutive-sequence/description/

const longestConsecutive = (nums) => {
    let set = new Set(nums)
    let longVal = 0

    for(n of set) {
        let lcVal = 0
        if(!set.has(n-1)) {
            while(set.has(n + lcVal)) {
                lcVal += 1
            }
            longVal = Math.max(lcVal, longVal)
        }
    }

    return longVal
}

console.log(longestConsecutive([100,4,200,1,3,2]))
console.log(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))