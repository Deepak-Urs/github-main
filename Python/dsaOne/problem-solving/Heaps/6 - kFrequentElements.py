import heapq

def kFrequentElements(arr, k):
    hm = {}
    minH = []
    for i in arr:
        hm[i] = hm.get(i, 0) + 1
    
    for i in hm:
        heapq.heappush(minH, [hm[i], i])
        if len(minH) > k:
            heapq.heappop(minH)
    
    for ix in range(k-1, -1, -1):
        print(minH[ix][1])

kFrequentElements([1,1,1,2,4,2,3], 2)