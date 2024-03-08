import sys

def mcmMemoization(arr, i, j):
    if i >= j: 
        memo[i][j] = 0
        return 0
    ans = sys.maxsize

    if memo[i][j] != -1:
        return memo[i][j]
    
    for k in range(i, j):
        tempAns = mcmMemoization(arr, i, k) + mcmMemoization(arr, k+1, j) + arr[i-1]*arr[j]*arr[k]

        if tempAns < ans:
            ans = tempAns
    print(memo)
    memo[i][j] = ans
    return memo[i][j]

ar = [40, 20, 30, 10, 30]
l = len(ar)
memo = [[] for _ in range(l)]
for i in range(l):
    memo[i] = [-1 for _ in range(l)]
#print(memo)

print(mcmMemoization(ar, 1, l-1))