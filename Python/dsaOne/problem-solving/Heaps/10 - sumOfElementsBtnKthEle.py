import heapq

def sumOfElementsBtnKthEle(arr, k1, k2):
    sm = 0
    minH = []

    for i in arr:
        heapq.heappush(minH, i)
    
    for k in range(len(minH)):
        if k1-1 < k < k2-1:
            sm += minH[k]
    
    return sm

print(sumOfElementsBtnKthEle([1,4,3,2,11], 2, 5))
