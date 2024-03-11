def LCSRecursive(M, N, m, n):
    if n == 0 or m == 0:
        return 0
    if M[n-1] == N[n-1]:
        return 1 + LCSRecursive(M,N,m-1,n-1)
    elif M[n-1] != N[n-1]:
        return max(LCSRecursive(M,N,n-1,m), LCSRecursive(M,N,n,m-1))

a = 'abcdefgh'
b = 'abedcgl'
print(LCSRecursive(a, b, len(a)-1, len(b)-1))