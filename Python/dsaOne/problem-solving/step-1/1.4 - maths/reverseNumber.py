def reverseNum(n):
    num = n
    rev = 0

    while n != 0:
        digit = n % 10
        rev  = rev * 10 + digit
        n = n // 10

    return rev
    #num = str(n)
    #if len(num) == 0:
    #    return None
    #l = 0
    #r = len(num)-1

    #while(l <= r):
    #    temp = num[r]
    #    num[r] = num[l]
    #    num[l] = temp
    
    #return int(num)


    #num = str(n)
    #if len(num) == 0:
    #    return None

    #r = ''
    #for x in range(len(num)-1,-1,-1):
    #    r += 1
    
    #return int(r)

    return reversed(n)

print(reverseNum(123))
print(reverseNum(1))