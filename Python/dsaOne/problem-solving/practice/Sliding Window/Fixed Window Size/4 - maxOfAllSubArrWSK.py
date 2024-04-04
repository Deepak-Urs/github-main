def maxOfAllSubArrWSK(arr, k):
    i = 0
    j = 0
    size = len(arr)
    res = []

    while j < size:
        res.append(arr[j])
        ws = j-i+1

        if ws < k:
            j += 1
        elif ws == k:
            print(max(res))

            res.pop(0)
            j += 1
            i += 1
    

maxOfAllSubArrWSK([1,3,-1,-3,5,3,6,7], 3)