#https://leetcode.com/problems/valid-anagram/description/

def anagram(s, t):
    if len(s) != len(t):
        return False

    hs = {}
    ht = {}

    for i in s:
        if i not in hs:
            hs[i] = 1
        else:
             hs[i] += 1
    
    for j in t:
        if j not in ht:
            ht[j] = 1
        else:
            ht[j] += 1

    return hs == ht

print(anagram("anagram", "nagaram"))
print(anagram("rat", "car"))
