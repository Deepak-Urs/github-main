import heapq

def frequencySort(arr):
    hm = {}
    minH = []

    for i in arr:
        hm[i] = hm.get(i,0)+1
    
    for j in hm:
        heapq.heappush(minH, [-hm[j], -j])
    
    print(minH)
    while len(minH) > 0:
        res = heapq.heappop(minH)
        for l in range(-res[0]):
            print(-res[1])

frequencySort([2,1,1,1,4,2,3])
