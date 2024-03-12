def scrambledString(a, b):
    if a == b: return True
    if len(a) < 1: return False

    flag = False
    n = len(a)

    for i in range(1,n):
        sLA = a[:i] # string Left - A
        sRB = b[n-i:]
        sRA = a[n-i:]
        sLB = b[:i]

        cn1 = scrambledString(sLA, sRB) and scrambledString(sRA, sLB)
        cn2 = scrambledString(sLA, sLB) and scrambledString(sRA, sRB)

        if cn1 or cn2:
            flag = True
            break
    
    return flag


a = 'great'
b = 'rgeat'
def main():
    if len(a) != len(b): return False
    if a == '' and b == '': return True
    print(scrambledString(a,b))

main()