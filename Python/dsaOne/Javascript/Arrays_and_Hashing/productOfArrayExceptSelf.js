const productOfArrayExceptSelf = (nums) => {
    let res = []
    let prefix = 1
    let postfix = 1

    for(let i = 0; i < nums.length; i++) {
        res[i] = prefix
        prefix *= nums[i]
    }

    for(let j = res.length - 1; j > -1; j--) {
        res[j] *= postfix
        postfix *= nums[j]
    }

    return res
}

console.log(productOfArrayExceptSelf([1,2,3,4])) //[24,12,8,6]