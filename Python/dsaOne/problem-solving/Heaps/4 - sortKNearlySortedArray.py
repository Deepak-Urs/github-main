import heapq

def sortKNearlySortedArray(arr, k):
    minH = []
    res = []

    for i in arr:
        heapq.heappush(minH, i)

        if len(minH) > k:
            res.append(heapq.heappop(minH))
    
    while len(minH) > 0:
        res.append(heapq.heappop(minH))
    
    return res

print(sortKNearlySortedArray([6,5,3,2,8,10,9], 3))