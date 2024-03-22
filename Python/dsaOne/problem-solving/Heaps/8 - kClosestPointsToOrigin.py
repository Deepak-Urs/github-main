import heapq

def kClosestPointsToOrigin(arr, k):
    maxH = []
    for i in arr:
        heapq.heappush(maxH, [ -(i[0]*i[0]+i[1]*i[1]), [i[0], i[1]] ])

        if len(maxH) > k:
            heapq.heappop(maxH)
    
    print(maxH)
    while len(maxH) > 0:
        res = heapq.heappop(maxH)
        print(res[1])

kClosestPointsToOrigin(([[1,3], [-2,2], [5,8], [0,1]]), 2)