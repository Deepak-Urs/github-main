def sumZero(arr):
    l = 0
    r = len(arr) - 1

    for i in range(len(arr)):
        if l < r and arr[l] + arr[r] == 0:
            return [arr[l], arr[r]]
        elif arr[l] + arr[r] < 0:
            l += 1
        elif arr[l] + arr[r] > 0:    
            r -= 1
    
    return False

print(sumZero([-2,0,1,3])) #false
print(sumZero([1,2,3])) #false
print(sumZero([-3,-2,-1,0,1,2,3]) )#[-3,3]
print(sumZero([-4,-3,-2,-1,0,1,5,6])) #[-1,1]