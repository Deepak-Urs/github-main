def fibonacciN(n, a = 0, b = 1):
    #if n <= 1:
    #    return n
    
    #l = fibonacciN(n-1)
    #sl = fibonacciN(n-2)
    
    #return l + sl
    if n > 0:
        print(a)
        fibonacciN(n-1, b, a+b)


fibonacciN(5)