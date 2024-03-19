import heapq

def kthSmallestElement(arr, k):
    maxH = []
    n = len(arr)

    for num in arr:
        heapq.heappush(maxH, -num)
        if len(maxH) > k:
            heapq.heappop(maxH)
    
    return -maxH[0]

print(kthSmallestElement([7,10,4,3,20,15],3))
print(sorted([7,10,4,3,20,15]))

