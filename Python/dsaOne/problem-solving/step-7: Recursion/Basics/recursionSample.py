def recursiveMethod(n):
    if n < 1:
        print('n < 1')
        return
    else:
        recursiveMethod(n-1)
        print(n)

recursiveMethod(5)