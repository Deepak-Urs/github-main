def printNBitBinNos(one, zero, n, op, res): # #1s > #0s
    if n == 0:
        res.append(op)
        return
    
    op1 = op + "1"
    printNBitBinNos(one+1, zero, n-1, op1, res)
    
    if one > zero:
        op2 = op + "0"
        printNBitBinNos(one, zero+1, n-1, op2, res)

    return res

def main():
    ip = int(input("Enter n-bit input:\t"))
    op = ""
    one = 0
    zero = 0
    res = []
    print(printNBitBinNos(one, zero, ip, op, res))

main()