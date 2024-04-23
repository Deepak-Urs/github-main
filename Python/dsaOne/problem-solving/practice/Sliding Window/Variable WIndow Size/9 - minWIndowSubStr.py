def minWIndowSubStr(s ,t):
    i,j,hm,count,ans, size = 0,0,{},0,float('inf'),len(s)

    for c in t: hm[c] = hm.get(c, 0) + 1
    k = len(hm)

    while j < size:
        if s[j] in hm:
            hm[s[j]] -= 1
            if hm[s[j]] == 0:
                count += 1
        
        if count == k:
            ans = min(ans, j-i+1)
            while count == k:
                if s[i] in hm:
                    hm[s[i]] += 1
                    if hm[s[i]] == 1:
                        count -= 1
                ans = min(ans, j-i+1)
                i += 1
        
        j+=1

    return ans if ans != float('inf') else 0

                
    
print(minWIndowSubStr('tomptapta', 'tta'))