Wt = [1,3,4,5]
Vl = [2,4,5,7]
W = 10
n = len(Wt)

memo = [[] for i in range(n)]
for j in range(n):
    memo[j] = [-1 for i in range(W)]

def ZOKpRMemoization(Wt, Vl, W, n):
    if W == 0 or n == 0:
        return 0
    
    if memo[n-1][W-1] != -1:
        return memo[n-1][W-1]
    
    if Wt[n-1] <= W:
        memo[n-1][W-1] = max(Vl[n-1] + ZOKpRMemoization(Wt, Vl, W- Wt[n-1], n-1), ZOKpRMemoization(Wt, Vl, W, n-1))
    elif Wt[n-1] > W:
        memo[n-1][W-1] = ZOKpRMemoization(Wt, Vl, W, n-1)

    return memo[n-1][W-1]
    

print(ZOKpRMemoization(Wt, Vl, W, n))

