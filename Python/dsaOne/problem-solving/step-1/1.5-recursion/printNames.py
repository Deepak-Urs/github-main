def printNames(n):
    if n == 0:
        print('-----')
        return
    
    print('Deepak Urs')
    printNames(n-1)

printNames(2)
printNames(5)