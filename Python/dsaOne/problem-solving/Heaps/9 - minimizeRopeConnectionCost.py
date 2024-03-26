from heapq import heappop, heappush
def minimizeRopeConnectionCost(arr):
    cost = 0
    minH = []

    for i in arr:
        heappush(minH, i)
    print(minH)
    
    while len(minH) >= 2:
        f = heappop(minH)
        s = heappop(minH)

        cost += f + s
        heappush(minH, f+s)
    
    return cost

print(minimizeRopeConnectionCost([1,4,3,2,11]))

