def topKFrequentElements(nums, k):
    hm = {}
    arr = []

    for i in range(len(nums)+1):
        arr.append([])

    for i in nums:
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 1
        
    for n,c in hm.items():
        arr[c].append(n)

    res = []
    for i in range(len(arr)-1, 0 , -1):
        for n in arr[i]:
            res.append(n)
            if len(res) == k:
                return res

print(topKFrequentElements([1,1,1,2,2,3], 2))
print(topKFrequentElements([1], 1))