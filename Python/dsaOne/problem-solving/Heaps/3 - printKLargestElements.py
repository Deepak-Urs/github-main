import heapq

def printKLargestElements(arr, k):
    minHeap = []
    
    for i in arr:
        heapq.heappush(minHeap, i)

        if len(minHeap) > k:
            heapq.heappop(minHeap)
    
    while len(minHeap) > 0:
        print(minHeap[0])
        heapq.heappop(minHeap)

printKLargestElements([7,10,4,3,20,15], 3)