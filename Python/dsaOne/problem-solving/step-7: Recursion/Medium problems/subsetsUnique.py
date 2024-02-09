def subsetsUnique(ip, op, s):
    if len(ip) == 0:
        op = ""
        return
    
    op1 = op
    op2 = op + ip[0]

    if op1 not in s:
        s.append(op1)

    if op2 not in s:
        s.append(op2)
    
    ip = ip[1:]

    subsetsUnique(ip, op1, s)
    subsetsUnique(ip, op2, s)

    return s
    #return sorted(s)


def main():
    ip = input('Enter string:')
    op = ""
    s = []
    print(subsetsUnique(ip, op, s))

main()