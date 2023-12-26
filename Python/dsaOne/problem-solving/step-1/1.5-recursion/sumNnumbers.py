def sumNnumbers(n):
    #if n == 0:
    #    print(s)
    #    return None
    #sumNnumbers(n-1, s+n)
    if n == 0:
        return 0
    return n + sumNnumbers(n-1)

print(sumNnumbers(5))
print(sumNnumbers(10))