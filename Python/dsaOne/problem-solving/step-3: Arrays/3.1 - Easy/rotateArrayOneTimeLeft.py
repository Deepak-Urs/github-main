#https://leetcode.com/problems/rotate-array/

def rotateArrayOneTimeLeft(arr):
    t = arr[0]
    l = len(arr)-1

    for i in range(l):
        arr[i] = arr[i+1]
    
    arr[-1] = t

    return arr

print(rotateArrayOneTimeLeft([2,3,4,5,9]))
print(rotateArrayOneTimeLeft([1,2,3,4,5,6,7,8,9]))