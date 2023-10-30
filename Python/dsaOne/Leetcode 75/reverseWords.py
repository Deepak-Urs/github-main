#https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75

def reverseWords(s):
    sA = s.split(' ')
    sA = [x for x in sA if x != '']
    #print(sA)
    l = 0
    r = len(sA)-1

    while(l<r):
        temp = sA[l]
        sA[l] = sA[r]
        sA[r] = temp
        l += 1
        r -= 1
    
    return ' '.join(sA)
        

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))

