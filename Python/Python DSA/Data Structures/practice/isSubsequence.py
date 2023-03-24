def isSubsequence(str1, str2):
    l, r = 0, 0

    if len(str1) == 0 or len(str2) == 0:
        return True

    while r < len(str2):
        if str1[l] == str2[r]:
            l += 1
        if l == len(str1):
            return True
        r += 1
    
    return False

print(isSubsequence('hello', 'hello world')) # true
print(isSubsequence('sing', 'sting')) # true
print(isSubsequence('abc', 'abracadabra')) # true
print(isSubsequence('abc', 'acb')) # false