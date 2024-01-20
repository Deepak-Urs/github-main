#https://leetcode.com/problems/palindrome-linked-list/description/

def checkPalindrome(head):
    s = ''
    curr = head

    while curr:
        s += str(curr.val)

    l = 0
    r = len(s)-1

    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    
    return True