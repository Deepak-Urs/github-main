import sys

def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    return True


def optimizedPalindromePartitioningMemoization(s, i, j):
    if i >= j or isPalindrome(s, i, j):
        return 0
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    ans = sys.maxsize

    for k in range(i, j):
        #tempAns = 1 + optimizedPalindromePartitioningMemoization(s, i, k) + optimizedPalindromePartitioningMemoization(s, k+1, j)
        if memo[i][k] != -1:
            left = memo[i][k]
        else:
            left = optimizedPalindromePartitioningMemoization(s, i, k)
            memo[i][k] = left

        if memo[k+1][j] != -1:
            right = memo[k+1][j]
        else:
            right = optimizedPalindromePartitioningMemoization(s, k+1, j)
            memo[k+1][j] = right
        
        tempAns = 1 + left + right

        if tempAns < ans:
            ans = tempAns

    memo[i][j] = ans
    return memo[i][j]

s = 'train'
l = len(s)
memo = [[] for _ in range(l)]
for i in range(l):
    memo[i] = [-1 for j in range(l)]
print(optimizedPalindromePartitioningMemoization(s, 0, l-1))