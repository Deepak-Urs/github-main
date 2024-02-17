st = 'aabaabaa'
ptn = 'aaba' 

def countOccurancesOfAnagram(st, ptn):
    ss = len(st)
    ws = len(ptn)
    pC = {}
    for i in ptn:
        pC[i] = pC.get(i, 0)+1
    count = len(pC)
    ans = 0
    
    i = 0
    j = 0

    while j < ss:
        if st[j] in pC:
            pC[st[j]] -= 1
            if pC[st[j]] == 0:
                count -= 1
        
        if j-i+1 < ws:
            j += 1
        elif j-i+1 == ws:
            if count == 0:
                ans += 1
            
            if count == 0 and pC[st[i]] == 0:
                count += 1
            pC[st[i]] += 1
            i += 1

            j += 1

    return ans

print(countOccurancesOfAnagram(st, ptn))