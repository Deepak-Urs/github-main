Wt = [1,3,4,5]
Vl = [2,4,5,7]
W = 10
n = len(Wt)

t = [[0 if ix ==0 or jx ==0 else None for jx in range(W+1)] for ix in range(n+1)]
#prints(t)

def ZOKpTopDown(Wt, Vl, W, n):
    for i in range(1,n+1):
        for j in range(1, W+1):
            if Wt[i-1] <= j:
                t[i][j] = max(Vl[i-1] + t[i-1][j-Wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]

    print(t)
    return t[i][j]
    
    

print(ZOKpTopDown(Wt, Vl, W, n))

