#def reverseArray(arr):
#    if len(arr) == 0: return
#    l = 0
#    r = len(arr)-1

#    while(l <= r):
#        temp = arr[l]
#        arr[l] = arr[r]
#        arr[r] = temp
#        l += 1
#        r -= 1
    
#    return arr
#print(reverseArray([5,4,3,2,1]))


def reverseArrayRecursion(arr, l, r):
    if l < r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        reverseArrayRecursion(arr, l+1, r-1)

arr = [5,4,3,2,1]
reverseArrayRecursion(arr, 0, len(arr)-1)
print(arr)
    
