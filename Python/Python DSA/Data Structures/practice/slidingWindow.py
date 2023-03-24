def maxSubArraySum(arr, num):
    if len(arr) < num:
        return None
    
    tempSum = 0
    maxSum = 0

    for i in range(num):
        maxSum += arr[i]

    tempSum = maxSum
    
    for i in range(num, len(arr)):
        tempSum = tempSum - arr[i - num] + arr[i]
        maxSum = max(tempSum, maxSum)
    
    return maxSum

print(maxSubArraySum([2,6,9,2,1,8,5,6,3], 3))