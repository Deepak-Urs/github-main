def frequencyCounter(arr, sqArr):
    if len(arr) != len(sqArr):
        return False

    arrObj = {}
    for i in arr:
        if i in arrObj:
            arrObj[i] += 1
        else:
            arrObj[i] = 1
    
    sqArrObj = {}
    for i in sqArr:
        if i in sqArrObj:
            sqArrObj[i] += 1
        else:
            sqArrObj[i] = 1

    res = False
    for i in arr:
        if (i*i) in sqArrObj and arrObj[i] == sqArrObj[(i*i)]:
            res = True
        else:
            res = False
            break
            
    
    return res

print(frequencyCounter([1,2,3], [4,1,9])) # true
print(frequencyCounter([1,2,3], [1,9])) # false
print(frequencyCounter([1,2,1], [4,4,1])) # false