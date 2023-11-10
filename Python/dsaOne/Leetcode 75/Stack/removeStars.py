#https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75

def removeStars(strArr):
    sA = []
    for c in strArr:
        if c != '*':
            sA.append(c)
        else:
            sA.pop()

    return ''.join(sA)

print(removeStars("leet**cod*e"))
print(removeStars("erase*****"))