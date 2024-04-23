def pickKuniqueToys(st, k):
    i,j,size,res = 0,0,len(st), 0
    pC = {}

    while j < size:
        pC[st[j]] = pC.get(st[j], 0) + 1
        pCount = len(pC)

        if pCount < k:
            j += 1
        elif pCount == k:
            ws = j-i+1
            res = max(ws, res)
            j += 1
        elif pCount > k:
            while pCount > k:
                pC[st[i]] = pC.get(st[i], 0) - 1

                if pC[st[i]] == 0: del pC[st[i]]
                pCount = len(pC)
                i += 1
            j += 1
    
    return res



print(pickKuniqueToys('aabacbebebe', 2))