# pick toys in such a way that
#1) They have to selected in continuos order
#2) They can be of max two types but any number/quantity


def pickToys(arr, k):
    i = 0
    j = 0
    size= len(arr)
    uC = {}
    uCount = 0
    res = 0

    while j < size:
        uC[arr[j]] = uC.get(arr[j], 0) + 1
        uCount = len(uC)

        if uCount < k:
            j += 1
        elif uCount == k:
            l = j-i+1
            res = l if l > res else res
            j += 1
        elif uCount > k:
            while uCount > k:
                uC[arr[i]] = uC.get(arr[i], 0) - 1
                if uC[arr[i]] == 0:
                    del uC[arr[i]]
                uCount = len(uC)
                l = j-i+1
                i += 1
            j += 1
    
    return res


arr = 'abacaab'
print(pickToys(arr, 2))