def factorialN(n):
    if n == 0:
        return 1
    return n * factorialN(n-1)

print(factorialN(3))
print(factorialN(5))
