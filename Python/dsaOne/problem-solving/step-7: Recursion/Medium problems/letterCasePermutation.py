def letterCasePermutation(ip, op , res):
    if len(ip) == 0:
        #if op not in res:
        res.append(op)
        return

    if 48 <= ord(ip[0]) <= 57:
        op1 = op + ip[0]
        ip = ip[1:]
        
        letterCasePermutation(ip, op1, res)
    else:
        op1 = op + ip[0].lower()
        op2 = op + ip[0].upper()
        ip = ip[1:]

        letterCasePermutation(ip, op1, res)
        letterCasePermutation(ip, op2, res)

    return res


def main():
    ip = input("Enter input: \t")
    op = ""
    res = []
    print(letterCasePermutation(ip, op, res))

main()