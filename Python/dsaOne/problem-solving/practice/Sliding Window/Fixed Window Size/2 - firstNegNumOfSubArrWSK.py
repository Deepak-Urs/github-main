def firstNegNumOfSubArrWSK(arr, k):
    i, j, size = 0, 0, len(arr)
    res = []

    while j < size:
        if arr[j] < 0:
            res.append(arr[j])
        ws = j-i+1

        if ws < k:
            j += 1
        elif ws == k:
            if len(res) == 0: res.append(0)
            else:
                print(res[0])
                if arr[i] == res[0]:
                    res.pop(0)
                j += 1
                i += 1


firstNegNumOfSubArrWSK([12,-1,-7,8,-15,30,16,28],3)