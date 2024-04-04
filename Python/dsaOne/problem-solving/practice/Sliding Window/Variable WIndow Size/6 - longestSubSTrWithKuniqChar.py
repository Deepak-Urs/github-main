def longestSubSTrWithKuniqChar(st, k):
    i, j, size, res = 0, 0, len(st), 0
    
    uC = {}

    while j < size:
        uC[st[j]] = uC.get(st[j], 0) + 1
        uCount = len(uC)

        if uCount < k:
            j += 1
        elif uCount == k:
            l = j-i+1
            res = max(res, l)
            j += 1
        else:
            while uCount > k:
                uC[st[i]] -= 1
                if uC[st[i]] == 0:
                    del uC[st[i]]
                
                uCount -= 1
                j += 1
                i += 1
    
    return res

print(longestSubSTrWithKuniqChar('aabacbebebe', 3))