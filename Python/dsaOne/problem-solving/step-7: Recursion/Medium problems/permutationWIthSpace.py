def pws(ip, op):
    if len(ip) == 0:
        op = ""
        return
    
    op1 = op + '_' + ip[0]
    op2 = op + ip[0]

    ip = ip[1:]

    if 'a' and 'b' and 'c' in op1: print(op1)
    if 'a' and 'b' and 'c' in op2: print(op2)

    pws(ip, op1)
    pws(ip, op2)


def main():
    ip = input('Enter string:\t')
    op = ip[0]
    pws(ip[1:], op)

main()