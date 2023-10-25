#https://leetcode.com/problems/valid-anagram/

def validAnagram(s, t):
    hm = {}
    hm2 = {}

    for i in s:
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 1

    for j in t:
        if j in hm2:
            hm2[j] += 1
        else:
            hm2[j] = 1

    return hm == hm2

print(validAnagram('anagram', 'nagaram'))
print(validAnagram('test', 'sets'))