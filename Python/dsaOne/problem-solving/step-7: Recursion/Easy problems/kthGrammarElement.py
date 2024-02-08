def kthGrammar(n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    if n == 1 and k == 1:
        return 0

    mid = (pow(2, n-1))//2

    if k <= mid:
        return kthGrammar(n-1, k)
    else:
        return not kthGrammar(n-1, k-mid)
    
print(kthGrammar(1,1))
print(kthGrammar(2,2))