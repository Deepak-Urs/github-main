def bubbleSort(arr):
    l = len(arr)-1
    for i in range(l, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

print(bubbleSort([5,2,3,4,1]))
print(bubbleSort([28, 16, 10, 87, 5]))