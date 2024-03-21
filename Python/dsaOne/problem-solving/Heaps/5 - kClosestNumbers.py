import heapq

def kClosestNumbers(arr, k, x):
    maxH = []

    for i in arr:
        heapq.heappush(maxH, [-abs(i - x), i])

        if len(maxH) > k:
            heapq.heappop(maxH)
        
    while len(maxH) > 0:
        val = heapq.heappop(maxH)
        print(val[1])

kClosestNumbers([2,3,6,7,8,9], 3, 7)
