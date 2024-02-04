def pow(x,n):
    def helper(x,n):
        if x == 0: return 0
        if n == 0: return 1

        r = helper(x*x, n//2)
        return r if not n%2 else x*r
    
    res = helper(x, abs(n))
    return res if n >=0 else 1/res

print(pow(2, 10))
print(pow(2.1, 3))
print(pow(2, -2))