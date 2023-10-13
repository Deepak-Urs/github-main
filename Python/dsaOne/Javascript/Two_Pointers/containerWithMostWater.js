//https://leetcode.com/problems/container-with-most-water/description/

const containerWithMostWater = (heights) => {
    let minMaxVal = 0
    let l = 0;
    let r = heights.length - 1

    for(let i = 0; i < heights.length; i++) {
        let currArea = Math.min(heights[l], heights[r]) * (r-l)
        minMaxVal = Math.max(minMaxVal, currArea)
        if(heights[l] <= heights[r]) {
            l++;
        }
        else if(heights[l] > heights[r]) {
            r--;
        }
    }

    return minMaxVal
}

console.log(containerWithMostWater([1,2]))
console.log(containerWithMostWater([1,8,6,2,5,4,8,3,7]))
