def subsets(ip, op):
    if len(ip) == 0:
        op = " "
        return
    
    op1 = op
    op2 = op
    op2 += ip[0]

    #if op1 not in res:
    #    res.append(op1)

    #if op2 not in res:
    #    res.append(op2)

    print(op1)
    print(op2)

    ip = ip[1:]

    subsets(ip, op1)
    subsets(ip, op2)
    
    #return res

def main():
    ip = input("Enter input string:")
    op = " "
    #res = []
    print(subsets(ip, op))

main()

# T.C => O(2^n)
# S.C => O(n * 2^n)


