def longestSubSTrWithKuniqChar(st, k):
    i,j,size = 0, 0, len(st)
    pC, count, res = {}, 0, 0

    while j < size:
        pC[st[j]] = pC.get(st[j], 0) + 1
        count = len(pC)

        if count < k:
            j += 1
        elif count == k:
            ws = j-i+1
            res = max(ws, res)
            j += 1
        elif count > k:
            while count > k:
                pC[st[i]] = pC.get(st[i], 0) - 1
                
                if pC[st[i]] == 0:
                    del pC[st[i]]
                
                count = len(pC)
                i += 1
            j += 1
    
    return res



print(longestSubSTrWithKuniqChar('aabacbebebe', 3))