def pwcc(ip, op, k):
    if len(ip) == 0:
        op = ""
        return
    
    op1 = op + ip[0]
    op2 = op + ip[0].upper()

    ip = ip[1:]

    if len(op1) == k: print(op1)
    if len(op2) == k: print(op2)


    pwcc(ip, op1, k)
    pwcc(ip, op2, k)

    return


def main():
    ip = input("Enter input string:")
    op = ""
    pwcc(ip, op, len(ip))

main()