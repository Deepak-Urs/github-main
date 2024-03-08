import sys

def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    return True


def palindromePartitioning(s, i, j):
    if i >= j or isPalindrome(s, i, j):
        return 0
    
    ans = sys.maxsize

    for k in range(i, j):
        tempAns = 1 + palindromePartitioning(s, i, k) + palindromePartitioning(s, k+1, j)
        if tempAns < ans:
            ans = tempAns

    return ans

s = 'qnitind'
print(palindromePartitioning(s, 0, len(s)-1))