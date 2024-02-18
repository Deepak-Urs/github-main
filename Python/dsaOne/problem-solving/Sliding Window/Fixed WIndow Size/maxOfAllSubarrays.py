def maxOfAllSubarrays(arr, ws):
    mx = []
    mxs = []
    i = 0
    j = 0
    size = len(arr)
    
    while j < size:
        mxs.append(arr[j])

        if j-i+1 < ws:
            j += 1
        elif j-i+1 == ws:
            mx.append(max(mxs))
            
            mxs.pop(0)
            i+=1

            j+=1
    
    return mx

print(maxOfAllSubarrays([1,3,-1,-3,5,3,6,7], 3))
print(maxOfAllSubarrays([7,6,5,4,3,2,1], 3))
print(maxOfAllSubarrays([1,2,3,4,5,6,7,8,9], 3))