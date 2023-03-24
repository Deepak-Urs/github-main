import numpy as np

twoDArray = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(twoDArray)

def traverse2DArray(array):
    # for no. of rows
    for i in range(len(array)):
        # for no. of columns
        for j in range(len(array[0])):
            print(array[i][j])

def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index '+str(i)+' '+str(j)
    
    return 'Element not found'

newTDA = np.delete(twoDArray, 1, axis = 0)
print(newTDA)


# traverse2DArray(twoDArray)
# print(searchTDArray(twoDArray,10))


