def bubbleSort(arr, n):
    if n == 0: return

    for j in range(0, n-1):
        if(arr[j] > arr[j+1]):
            t = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = t
        
    bubbleSort(arr, n-1)

arr = [12,13,15,14,11]
bubbleSort(arr, len(arr))
print(arr)
