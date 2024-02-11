def solve(open, close, op, res):
    if open == 0 and close == 0:
        res.append(op)
        return
    
    if open != 0:
        op1 = op + "("
        solve(open-1, close, op1, res)

    if open < close:
        op2 = op + ")"
        solve(open, close-1, op2, res)

    return res


def generateAllBalancedParanthesis():
    ip = int(input("Enter paranthesis size:"))
    op = ""
    open = ip
    close = ip
    res = []
    print(solve(open, close, op, res))

generateAllBalancedParanthesis()