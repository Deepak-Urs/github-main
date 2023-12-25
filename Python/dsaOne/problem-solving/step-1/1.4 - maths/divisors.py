import math
def divisors(n):
    #c = []
    #for i in range(1, n+1):
    #    if n % i == 0:
    #        c.append(i)
    
    #return c
    
    c = []
    i = 1
    l = math.sqrt(n)
    while(i <= l):
        if n % i == 0:
            c.append(int(i))
            if i != n/i:
                c.append(int(n/i))
        i += 1

    return c

print(divisors(10))
print(divisors(36))
print(divisors(97))
    
