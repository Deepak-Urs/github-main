#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def stockBuySell(arr):
    l, r, maxP  = 0, 0, 0
    n = len(arr)

    while r < n:
        if arr[l] < arr[r]:
            profit = arr[r] - arr[l]
            maxP = max(maxP, profit)
        else:
            l = r
        
        r += 1
    
    return maxP

print(stockBuySell([7,1,5,3,6,4]))
print(stockBuySell([7,6,4,3,1]))
