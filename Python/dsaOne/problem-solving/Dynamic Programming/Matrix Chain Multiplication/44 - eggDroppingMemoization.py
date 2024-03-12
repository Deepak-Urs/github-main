import sys

def eggDroppingMemoization(e, f):
    if e == 1:
        return f
    
    if f == 0 or f == 1:
        return f
    
    if m[e-1][f-1] != -1:
        return m[e-1][f-1]
    
    mn = sys.maxsize
    i = 1
    j = f+1

    for k in range(i, j):
        tempAns = 1 + max(eggDroppingMemoization(e-1, k-1), eggDroppingMemoization(e, f-k))
        mn = min(mn, tempAns)
        
    m[e-1][f-1] = mn
    return m[e-1][f-1]

ee = 3
ff = 5
m = [[] for i in range(ee)]
for i in range(ee):
    m[i] = [-1 for j in range(ff)]
print(eggDroppingMemoization(ee,ff))