def selectionSort(arr):
    l = len(arr)-1
    for i in range(0, l-1):
        mn = i
        for j in range(i+1, l+1):
            if arr[j] < arr[i]:
                mn = j
        temp = arr[i]
        arr[i] = arr[mn]
        arr[mn] = temp

    return arr

print(selectionSort([5,2,3,4,1]))
print(selectionSort([28, 16, 10, 87, 5]))