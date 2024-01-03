from math import inf
def findMaxSubArray(arr, n):
    maxVal = -inf
    summ = 0
    start = 0
    ansStart, ansEnd = -1, -1

    for i in range(n):
        if summ == 0:
            start = i
        
        summ += arr[i]
        
        if summ > maxVal:
            maxVal = summ

            ansStart = start
            ansEnd = i

        if summ < 0:
            summ = 0

    r = '['
    for i in range(ansStart, ansEnd+1):
        r += str(arr[i])
        if i is not ansEnd:
             r += ', '
    r += ']'
    print(r)


ar = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(ar)
findMaxSubArray(ar, n)
            