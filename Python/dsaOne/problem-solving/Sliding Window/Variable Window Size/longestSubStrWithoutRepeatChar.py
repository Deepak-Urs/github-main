def longestSubStrWithoutRepeatChar(st):
    i = 0
    j = 0
    size = len(st)
    uC = {}
    res = 0

    while j < size:
        uC[st[j]] = uC.get(st[j], 0) + 1
        uCount = len(uC)
        l = j-i+1

        if uCount < l:
            while uCount < l:
                uC[st[i]] = uC.get(st[i], 0) - 1
                if uC[st[i]] == 0:
                    del uC[st[i]]
                uCount = len(uC)
                i += 1
                l = j-i+1
            j += 1
        elif uCount == l:
            res = l if l > res else res
            j += 1
        
    return res


print(longestSubStrWithoutRepeatChar('pwwkew'))