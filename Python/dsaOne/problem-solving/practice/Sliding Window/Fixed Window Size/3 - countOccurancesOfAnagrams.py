def countOccurancesOfAnagrams(st, sub):
    i, j, size, ws = 0, 0, len(st), len(sub)
    pC, res = {}, 0
    for v in sub: pC[v] = pC.get(v,0) + 1
    l = len(pC)

    while j < size:
        if st[j] in pC:
            pC[st[j]] -= 1

            if pC[st[j]] == 0:
                l -= 1

        w = j-i+1

        if w < ws:
            j += 1
        elif w == ws:
            if l == 0:
                res += 1

                if pC[st[i]] == 0:
                    l += 1
            
            pC[st[i]] += 1
            i += 1
            j += 1
    
    return res
                


print(countOccurancesOfAnagrams('aabaabaa', 'aba'))