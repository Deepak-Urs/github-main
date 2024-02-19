def longestSubStrWithKuniqueChar(st, k):
    i = 0
    j = 0
    size = len(st)
    uC = {}
    res = 0

    while j < size:
        uC[st[j]] = uC.get(st[j], 0) + 1
        uCount = len(uC)

        if uCount < k:
            j += 1
        elif uCount == k:
            l = j-i+1
            res = l if l > res else res
            j += 1
        elif uCount > k:
            while uCount > k:
                uC[st[i]] = uC.get(st[i], 0) - 1
                if uC[st[i]] == 0:
                    del uC[st[i]]
                uCount = len(uC)
                i += 1
            j += 1
    
    return res


print(longestSubStrWithKuniqueChar('aabacbebebe', 3))
#
#