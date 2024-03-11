def ZOKpRecursive(Wt, Vl, W, n):
    V = 0
    if W == 0 or n == 0:
        return 0
    
    if Wt[n-1] <= W:
        V = max(Vl[n-1] + ZOKpRecursive(Wt, Vl, W- Wt[n-1], n-1), ZOKpRecursive(Wt, Vl, W, n-1))
    elif Wt[n-1] > W:
        V = ZOKpRecursive(Wt, Vl, W, n-1)

    return V
    
Wt = [1,3,4,5]
Vl = [2,4,5,7]
W = 10
n = len(Wt)
print(ZOKpRecursive(Wt, Vl, W, n))

