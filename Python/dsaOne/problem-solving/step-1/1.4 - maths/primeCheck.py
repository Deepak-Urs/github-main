def primeCheck(n):
    c = 0
    for i in range(1, n):
        if n % i == 0:
            c += 1

    return 'YES' if c <= 2 else "NO"


n = int(input())
print(primeCheck(n))