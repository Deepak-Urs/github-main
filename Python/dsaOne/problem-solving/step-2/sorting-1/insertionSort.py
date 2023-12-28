def insertionSort(arr):
    l = len(arr)-1
    for i in range(l+1):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            t = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = t
            j -= 1

    return arr

print(insertionSort([5,4,3,2,1]))
