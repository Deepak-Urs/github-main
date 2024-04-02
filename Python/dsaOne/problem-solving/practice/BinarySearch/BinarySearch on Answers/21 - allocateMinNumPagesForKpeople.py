def allocateMinNumPagesForKpeople(arr, k):
    st = max(arr)
    en = sum(arr)
    res = -1

    while st <= en:
        m = st + (en-st)//2

        if isValid(arr, m, k):
            res = m
            en = m - 1
        else:
            st = m + 1

    return res

def isValid(arr, m, k):
    count = 1
    sm = 0
    for i in arr:
        sm += i

        if sm > m:
            count += 1
            sm = i
        
        if count > k:
            return False
    return True

print(allocateMinNumPagesForKpeople([10,20,30,40], 2))
