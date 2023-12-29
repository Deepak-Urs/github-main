def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]

def pivot(arr, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            swap(arr, swap_index, i)
        swap(arr, pivot_index, swap_index)
    return swap_index

def quickSortHelper(arr, left, right):
    if left < right:
        pivot_index = pivot(arr, left, right)
        quickSortHelper(arr, left, pivot_index-1)
        quickSortHelper(arr, pivot_index+1, right)
    
    return arr

def quickSort(arr):
    return quickSortHelper(arr, 0, len(arr)-1)

arr= [2,3,1,5,4]
print(quickSort(arr))
