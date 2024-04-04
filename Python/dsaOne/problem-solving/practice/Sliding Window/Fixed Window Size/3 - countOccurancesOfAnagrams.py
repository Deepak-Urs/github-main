def countOccurancesOfAnagrams(st, sub):
    i, j = 0, 0
    size = len(st)
    ws = len(sub)

    pC = {}
    for v in sub:
        pC[v] = pC.get(v, 0) + 1
    pcL = len(pC)

    ans = 0


    while j < size:
        if st[j] in st: 
            pC[st[j]] -= 1
            if pC[st[j]] == 0:
                pcL -= 1
        w = j-i+1

        if w < ws:
            j += 1
        else:
            if pcL == 0:
                ans += 1
            
            if pcL == 0 and pC[st[i]] == 0:
                pcL += 1
                
            pC[st[i]] += 1
            j += 1
            i += 1

    return ans


print(countOccurancesOfAnagrams('aabaabaa', 'aba'))