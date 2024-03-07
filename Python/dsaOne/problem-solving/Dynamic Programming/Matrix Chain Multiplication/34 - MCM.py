import sys

def mcm(arr, i, j):

    if i >= j:
        return 0
    ans = sys.maxsize
    
    for k in range(i, j):
        tempAns = mcm(arr, i, k) + mcm(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
        if tempAns < ans:
            ans = tempAns

    return ans

ar = [40, 20, 30, 10, 30]
print(mcm(ar, 1, len(ar)-1))