def minWindowSubstring(s, t):
    hm = {}
    for c in t:
        hm[c] = hm.get(c, 0) + 1
    
    k = len(hm)
    count = 0
    n = len(s)
    i = 0
    j = 0
    ans = float('inf')
    
    while j < n:
        if s[j] in hm:
            hm[s[j]] -= 1
            if hm[s[j]] == 0:
                count += 1
        
        if count == k:
            ans = min(ans, j - i + 1)
            while count == k:
                if s[i] in hm:
                    hm[s[i]] += 1
                    if hm[s[i]] == 1:
                        count -= 1
                ans = min(ans, j - i + 1)
                i += 1

        j += 1
    
    return ans if ans != float('inf') else 0

s = "tomtaptat"
t = "tta"
result = minWindowSubstring(s, t)
print("Minimum Window Substring is:", result)
