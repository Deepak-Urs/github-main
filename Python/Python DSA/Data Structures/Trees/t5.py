def getOriginalMatrix(transformedMatrix):
    sum = 0
    res = transformedMatrix
    for i in range(len(res)):
        for j in range(len(res[0])):
            sum  = res[i][j] + sum
            res[i][j] = sum
    
    print(sum)
    return res

print(getOriginalMatrix([[1,2,3], [4,5,6]]))
# [2,3]
# [5,7]