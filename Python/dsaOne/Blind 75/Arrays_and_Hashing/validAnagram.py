#https://leetcode.com/problems/valid-anagram/description/

def validAnagram(s, t):
    hm1 = {}
    hm2 = {}

    for i in s:
        if i in hm1:
            hm1[i] += 1
        else:
            hm1[i] = 1
    
    for j in t:
        if j in hm2:
            hm2[j] += 1
        else:
            hm2[j] = 1

    return hm1 == hm2

print(validAnagram('anagram', 'nagaram'))
print(validAnagram('anagam', 'agaram'))
