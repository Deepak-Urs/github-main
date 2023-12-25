def isArmstrong(n):
    """
    :type n: int
    :rtype: bool
    """
    n = str(n)
    l = len(n)
    s = 0
    for i in n:
        s += pow(int(i), l)
    
    return int(n) == s
        
print(isArmstrong(153))
print(isArmstrong(370))
print(isArmstrong(156))
