import sys

def eggDropping(e, f):
    if e == 1:
        return f
    
    if f == 0 or f == 1:
        return f
    
    mn = sys.maxsize
    i = 1
    j = f

    for k in range(i, j):
        tempAns = 1 + max(eggDropping(e-1, k-1), eggDropping(e, f-k))
        mn = min(mn, tempAns)
    
    return mn

print(eggDropping(3,5))