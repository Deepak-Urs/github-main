#https://leetcode.com/problems/group-anagrams/description/

def groupAnagrams(strs):
    hm = {}

    for i in strs:
        val = "".join(sorted(i))
        if val in hm:
            hm[val].append(i)
        else:
            hm[val] = [i]
    
    res = []
    for i in hm:
        res.append(hm[i])

    return res

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))