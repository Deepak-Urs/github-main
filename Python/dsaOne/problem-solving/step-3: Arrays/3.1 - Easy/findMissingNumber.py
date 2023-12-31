#https://leetcode.com/problems/missing-number/description/

def findMissingNumber(arr):
    n = len(arr) + 1
    for i in range(n):
        if i not in arr:
            return i

print(findMissingNumber([0,1,2,3,4,6,7]))
print(findMissingNumber([0,1]))
