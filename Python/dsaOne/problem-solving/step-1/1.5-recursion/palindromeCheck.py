#def palindromeCheck(s):
#    l = 0
#    r = len(s)-1
#    while(l < r):
#        if not s[l] == s[r]:
#            return "Not Palindrome"
#        l += 1
#        r -= 1
    
#    return "Palindrome"

#s = 'ABCDCBA'
#s2 = 'tuf'
#print(palindromeCheck(s))
#print(palindromeCheck(s2))


def palindromeCheckRecursion(s, l, r):
    if l < r:
        if s[l] != s[r]:
            return "Not palindrome"
        palindromeCheckRecursion(s, l+1, r-1)
    
    return "Palindrome"

s = 'ABCDCBA'
s2 = 'tuf'
print(palindromeCheckRecursion(s, 0, len(s)-1))
print(palindromeCheckRecursion(s2, 0, len(s2)-1))