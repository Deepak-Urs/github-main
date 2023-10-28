#https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

def reverseVowels(s):
    l = 0
    r = len(s) - 1
    vs = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sA = list(s)

    while(l < r):
        if(sA[l] in vs and sA[r] in vs):
            temp = sA[l]
            sA[l] = sA[r]
            sA[r] = temp
            l += 1
            r -= 1
        while(sA[l] not in vs):
            l += 1
        while(sA[r] not in vs):
            r -= 1

    return ''.join(sA)

print(reverseVowels('hello'))
print(reverseVowels('leetcode'))