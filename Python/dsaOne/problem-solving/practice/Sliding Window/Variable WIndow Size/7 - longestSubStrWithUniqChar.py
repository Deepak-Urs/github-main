def longestSubStrWithUniqChar(st):
    i,j,size,res = 0,0,len(st),0
    uC, uCount = {}, 0

    while j < size:
        uC[st[j]] = uC.get(st[j], 0) + 1
        uCount = len(uC)
        ws = j-i+1

        if uCount == ws:
            res = max(ws, res)
            j += 1
        elif uCount < ws:
            while uCount < ws:
                uC[st[i]] = uC.get(st[i], 0) - 1
                if uC[st[i]] == 0:
                    del uC[st[i]]
                
                uCount = len(uC)
                i += 1
                ws = j-i+1
            j += 1
    
    return res
            
    

print(longestSubStrWithUniqChar('pwwkew'))
