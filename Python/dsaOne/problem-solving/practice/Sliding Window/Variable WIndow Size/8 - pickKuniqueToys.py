def pickKuniqueToys(st, k):
    i, j, size, res = 0, 0, len(st), 0
    uC, uCount = {}, 0

    while j < size:
        uC[st[j]] = uC.get(st[j], 0) + 1
        uCount = len(uC)

        if uCount < k:
            j += 1
        elif uCount == k:
            l = j-i+1
            res = max(l, res)
            j += 1
        else:
            while uCount > k:
                uC[st[i]] -= 1

                if uC[st[i]] == 0:
                    del uC[st[i]]
                
                i += 1
                uCount = len(uC)
            j += 1
    
    return res



print(pickKuniqueToys('aabacbebebe', 2))