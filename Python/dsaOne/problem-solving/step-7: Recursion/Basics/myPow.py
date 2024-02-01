def myPow(x,n):
    if n == 0:
        return 1
    elif n < 0:
        return 1/(x * myPow(x, n+1))
    return x * myPow(x, n-1)

print(myPow(4,-2))