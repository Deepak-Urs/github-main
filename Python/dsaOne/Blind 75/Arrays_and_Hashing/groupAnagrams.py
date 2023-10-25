#https://leetcode.com/problems/group-anagrams/description/

def groupAnagrams(strs):
    hm = {}
    for i in strs:
        res = ''.join(sorted(i))

        if res in hm:
            hm[res].append(i)
        else:
            hm[res] = [i]
        
    res = []
    for j in hm:
        res.append(hm[j])
    
    return res

print(groupAnagrams(['ate', 'eat', 'tan', 'can', 'ant']))
print(groupAnagrams([]))
        
    