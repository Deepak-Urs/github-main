def findValInSortedMatrix(arr, t):
    n, m = len(arr), len(arr[0])

    i = 0
    j = m - 1

    while i >= 0 and i < n and j >= 0 and j < m:
        print(arr[i][j])
        if t == arr[i][j]:
            return [i, j]
        elif t < arr[i][j]:
            j -= 1
        else:
            i += 1
        
    
    return -1

print(findValInSortedMatrix([[10,20,30,40], [15,25,35,45], [27,29,37,45], [32,33,39,59]], 29))