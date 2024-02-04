def printNto1(n):
    if n == 1:
        print(1)
        return
    print(n)
    printNto1(n-1)

printNto1(7)