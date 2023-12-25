def printNos(n):
    if n == 6:
        return
    
    print(n)
    printNos(n+1)

printNos(1)