def firstNegNumOfSubArrWSK(arr, k):
    i, j, size = 0, 0, len(arr)
    res = []

    while j < size:
        if arr[j] < 0:
            res.append(arr[j])
        w = j-i+1

        if w < k:
            j += 1
        elif w == k:
            l = len(res)
            if l != 0:
                print(res[0])
            else:
                print(0)

            if l != 0 and arr[i] == res[0]:
                res.pop(0)
            i += 1
            j += 1



firstNegNumOfSubArrWSK([12,-1,-7,8,-15,30,16,28],3)