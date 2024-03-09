def evaluateExpressionToTrueMemo(s, i, j, isTrue):    
    if i >= j:
        if isTrue: return s[i] == 'T'
        else: return s[i] == 'F'
    
    ans = 0
    key = str(i) + ' ' + str(j) + ' ' + str(isTrue)

    if key in mp:
        return mp[key]

    for k in range(i+1, j, 2):
        lT = evaluateExpressionToTrueMemo(s, i, k-1, True)
        lF = evaluateExpressionToTrueMemo(s, i, k-1, False)
        rT = evaluateExpressionToTrueMemo(s, k+1, j, True)
        rF = evaluateExpressionToTrueMemo(s, k+1, j, False)

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
        
        mp[key] = ans
    
    return mp[key]

exp = 'T|F&T^F'
mp = {}
print(evaluateExpressionToTrueMemo(exp, 0, len(exp)-1, True))