import sys

def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    return True


def palindromePartitioningMemoization(s, i, j):
    if i >= j or isPalindrome(s, i, j):
        return 0
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    ans = sys.maxsize

    for k in range(i, j):
        tempAns = 1 + palindromePartitioningMemoization(s, i, k) + palindromePartitioningMemoization(s, k+1, j)
        if tempAns < ans:
            ans = tempAns

    memo[i][j] = ans
    return memo[i][j]

s = 'qnitid'
l = len(s)
memo = [[] for _ in range(l)]
for i in range(l):
    memo[i] = [-1 for j in range(l)]
print(palindromePartitioningMemoization(s, 0, l-1))