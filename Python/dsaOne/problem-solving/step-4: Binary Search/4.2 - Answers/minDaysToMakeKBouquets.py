#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

def minDays(bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        val = m * k
        n = len(bloomDay)

        if val > n:
            return -1

        low = float('inf')
        high = float('-inf')

        for i in range(n):
            low = min(low, bloomDay[i])
            high = max(high, bloomDay[i])

        while low <= high:
            mid = (low+high)//2

            if isPossible(bloomDay, mid, m, k):
                high = mid -1
            else:
                low = mid + 1
            
        return low

def isPossible(arr, day, m , k):
    n = len(arr)
    ct = 0
    nB = 0

    for i in range(n):
        if arr[i] <= day:
            ct += 1
        else:
            nB += ct//k
            ct = 0
    
    nB += ct//k
    return nB >= m
    
    
print(minDays([1,10,3,10,2], 3, 2))
print(minDays([1,10,3,10,2], 3, 1))
print(minDays([7,7,7,7,12,7,7], 2, 3))
