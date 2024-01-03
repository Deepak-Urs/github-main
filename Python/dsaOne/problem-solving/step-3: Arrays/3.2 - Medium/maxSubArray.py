#https://leetcode.com/problems/maximum-subarray/description/
def maxSubArray(arr):
    maxSum = arr[0]
    curSum = arr[0]

    for i in range(1,len(arr)):
        curSum = arr[i] + max(curSum, 0)
        maxSum = max(maxSum, curSum)
    
    return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))


    