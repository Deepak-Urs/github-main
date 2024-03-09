def evaluateExpressionToTrue(s, i, j, isTrue):    
    if i >= j:
        if isTrue: return s[i] == 'T'
        else: return s[i] == 'F'
    
    ans = 0

    for k in range(i+1, j, 2):
        lT = evaluateExpressionToTrue(s, i, k-1, True)
        lF = evaluateExpressionToTrue(s, i, k-1, False)
        rT = evaluateExpressionToTrue(s, k+1, j, True)
        rF = evaluateExpressionToTrue(s, k+1, j, False)

        if s[k] == '&':
            if isTrue:
                ans += lT * rT
            else:
                ans += lT * rF + lF * rT + lF * rF
        elif s[k] == '|':
            if isTrue:
                ans += lT * rT + lT * rF + lF * rT
            else:
                ans += lF * rF
        elif s[k] == '^':
            if isTrue:
                ans += lT * rF + lF * rT
            else:
                ans += lT * rT + lF * rF
    
    return ans

exp = 'T|F&T^F'
print(evaluateExpressionToTrue(exp, 0, len(exp)-1, True))