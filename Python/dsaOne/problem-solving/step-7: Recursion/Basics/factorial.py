def factorial(n):
    assert int(n) == n and n >= 0, 'Enter a positive number'
    if n in [0,1]:
        return 1
    return n * factorial(n-1)

print(factorial(4))
print(factorial(5))
print(factorial(10))