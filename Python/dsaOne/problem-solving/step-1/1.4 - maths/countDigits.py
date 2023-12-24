def countDigits(n):
    n = str(n)
    return len(n)

# coding ninjas vcariant problem
#def countDigits(n):
#    num = str(n)
#    c = 0
#    l = 0
#    lc = 0
#    r = len(num)-1

#    while(l <= r and lc < len(num)):
#        if n % int(num[l])== 0:
#            l += 1
#            c += 1
#        elif n % int(num[r])== 0:
#            r -= 1
#            c += 1
#        lc += 1
    
#    return c


print(countDigits(336))
print(countDigits(373))
print(countDigits(35))