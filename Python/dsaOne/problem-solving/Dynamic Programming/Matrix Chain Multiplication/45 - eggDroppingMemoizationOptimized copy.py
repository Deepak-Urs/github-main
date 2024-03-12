import sys

def eggDroppingMemoizationOptimized(e, f):
    if e == 1:
        return f
    
    if f == 0 or f == 1:
        return f
    
    if dp[e-1][f-1] != -1:
        return dp[e-1][f-1]
    
    mn = sys.maxsize
    i = 1
    j = f+1

    for k in range(i, j):
        #tempAns = 1 + max(eggDroppingMemoizationOptimized(e-1, k-1), eggDroppingMemoizationOptimized(e, f-k))
        if dp[e-2][k-2] != -1:
            low = dp[e-2][k-2]
        else:
            low = eggDroppingMemoizationOptimized(e-1, k-1)
            dp[e-2][k-2] = low
        
        if dp[e-1][f-k-1] != -1:
            high = dp[e-1][f-k-1]
        else:
            high = eggDroppingMemoizationOptimized(e, f-k)
            dp[e-1][f-k-1] = high

        tempAns = 1 + max(low, high)
        mn = min(mn, tempAns)
        
    dp[e-1][f-1] = mn
    return dp[e-1][f-1]

ee = 3
ff = 5
dp = [[] for i in range(ee)]
for i in range(ee):
    dp[i] = [-1 for j in range(ff)]
print(eggDroppingMemoizationOptimized(ee,ff))