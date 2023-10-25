#https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

def mergeStringsAlternatively(s1, s2):
    l = 0
    r = 0
    res = ''

    while(l < len(s1) and r < len(s2)):
        res = res + s1[l] + s2[r]
        l = l + 1
        r = r + 1

    if(l < len(s1)):
        res = res + s1[l:]
    elif(r < len(s2)):
        res = res + s2[r:]

    return res

print(mergeStringsAlternatively('abc', 'pqr'))
print(mergeStringsAlternatively('ab', 'pqrs'))
print(mergeStringsAlternatively('abcd', 'pq'))