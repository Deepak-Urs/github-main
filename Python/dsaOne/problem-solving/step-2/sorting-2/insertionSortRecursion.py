def insertionSortRecursion(arr , n, l):
    if n == l+1: return

    i = n
    while i > 0 and arr[i-1] > arr[i]:
        t = arr[i-1]
        arr[i-1] = arr[i]
        arr[i] = t
        i -= 1

    insertionSortRecursion(arr, n+1, l) 

arr = [96, 99, 98, 95, 97]
insertionSortRecursion(arr, 0, len(arr)-1)
print(arr)