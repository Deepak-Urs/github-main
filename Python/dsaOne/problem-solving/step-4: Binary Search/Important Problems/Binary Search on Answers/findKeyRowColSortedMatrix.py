def findKeyRowColSortedMatrix(arr, t):
    m = len(arr)
    n = len(arr[0])

    i = 0
    j = m-1

    while i >= 0 and i < n and j >= 0 and j < m:
        if arr[i][j] == t:
            return [i,j]
        elif t < arr[i][j]:
            j -= 1
        elif t > arr[i][j]:
            i += 1
        print(arr[i][j])

    return -1

print(findKeyRowColSortedMatrix([[10,20,30,40], [15,25,35,45], [27,29,37,45], [32,33,39,59]], 21))