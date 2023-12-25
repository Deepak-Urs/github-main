def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    num = str(x)
    if len(num) == 0: return None

    l = 0
    r = len(num)-1

    while(l <= r):
        if(num[l] != num[r]):
            return False
        l += 1
        r -= 1

    return True

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))