def maxOfAllSubArrWSK(arr, k):
    i,j,size = 0,0, len(arr)
    res = []

    while j < size:
        res.append(arr[j])
        w = j-i+1

        if w < k:
            j += 1
        elif w == k:
            print(max(res))

            res.pop(0)
            i += 1
            j += 1
        

maxOfAllSubArrWSK([1,3,-1,-3,5,3,6,7], 3)