def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(3,6))
print(gcd(8,4))
print(gcd(2,19))
