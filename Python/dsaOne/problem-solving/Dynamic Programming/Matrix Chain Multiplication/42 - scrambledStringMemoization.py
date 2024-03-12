def scrambledStringMemo(a, b):
    if a == b: return True
    if len(a) < 1: return False

    key = str(a) + str(b)
    if key in mp:
        return mp[key]
    
    flag = False
    n = len(a)

    for i in range(1,n):
        sLA = a[:i] # string Left - A
        sRB = b[n-i:]
        sRA = a[n-i:]
        sLB = b[:i]

        cn1 = scrambledStringMemo(sLA, sRB) and scrambledStringMemo(sRA, sLB)
        cn2 = scrambledStringMemo(sLA, sLB) and scrambledStringMemo(sRA, sRB)

        if cn1 or cn2:
            #flag = True
            #mp[key] = flag
            #break
            return True
        
        mp[key] = flag

    #print(mp)
    #print(key)
    return flag


a = 'great'
b = 'rgeat'
mp = {}
def main():
    if len(a) != len(b): return False
    if a == '' and b == '': return True
    print(scrambledStringMemo(a,b))

main()