def sort(arr):
    #base condition
    if len(arr) == 1:
        return arr
    
    #hypothesis
    t = arr.pop()
    sort(arr)
    insert(arr, t)
    return arr

# induction
def insert(arr, t):
    if len(arr) == 0 or arr[len(arr)-1] <= t:
        arr.append(t)
        return
    
    t2 = arr.pop()
    insert(arr, t)
    arr.append(t2)


print(sort([0,1,5,2]))
print(sort([0,1,5,2,4,3,11,8,6]))
    