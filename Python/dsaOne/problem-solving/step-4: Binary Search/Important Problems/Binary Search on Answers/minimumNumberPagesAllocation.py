def isValid(arr, n, mE):
    std = 1
    sum = 0 

    for i in arr:
        sum += i
        if sum > mE:
            std += 1
            sum = i
        if std > n:
            return False
    
    return True

def minimumNumberPagesAllocation(arr, n):
    if n > len(arr):
        return -1
    
    st = max(arr)
    en = sum(arr)
    res = -1

    while st <= en:
        m = st + (en-st)//2

        if(isValid(arr, n, m)):
            res = m
            en = m - 1
        else:
            st = m + 1

    return res

print(minimumNumberPagesAllocation([10,20,30,40], 2))