#https://leetcode.com/problems/valid-palindrome/

def validPalindrome(s):
    l = 0
    r = len(s)-1

    while(l < r):
        while(l < r and not isalnum(s[l])):
            l += 1
        
        while(l < r and not isalnum(s[r])):
            r -= 1

        if(s[l].lower() != s[r].lower()):
            return False

        l += 1
        r -= 1

    return True


def isalnum(c):
    if((ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))):
        return True
    else:
        return False


print(validPalindrome('A man, a plan, a canal: Panama'))
print(validPalindrome('race a car'))