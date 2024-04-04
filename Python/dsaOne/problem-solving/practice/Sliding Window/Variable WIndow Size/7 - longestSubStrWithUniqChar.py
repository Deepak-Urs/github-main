def longestSubStrWithUniqChar(st):
    i, j, size, res = 0, 0, len(st), 0
    uC, uCount = {}, 0

    while j < size:
        uC[st[j]] = uC.get(st[j], 0) + 1
        uCount = len(uC)
        l = j-i+1

        if uCount < l:
            while uCount < l:
                uC[st[i]] = uC.get(st[i], 0) - 1

                if uC[st[i]] == 0:
                    del uC[st[i]]
                
                uCount= len(uC)
                i += 1
                l = j - i + 1
            j += 1

        elif uCount == l:
            res = max(res, l)
            j += 1

    return res


print(longestSubStrWithUniqChar('pwwkew'))
