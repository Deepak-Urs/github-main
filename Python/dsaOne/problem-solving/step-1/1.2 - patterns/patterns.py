# pattern-1: rectangular pattern
def pat1(n):
    print('Pattern - 1:\n')
    res = ''
    for i in range(n):
        for j in range(n):
            res += '* ' 
        #if i * j == (n-1)*(n-1): break
        res += '\n'
    return res

print(pat1(6))

# pattern-2 : right angled triangle pattern
def pat2(n):
    print('Pattern - 2:\n')
    r = ''
    for i in range(1, n+1):
        for j in range(0,i):
            r += '* '
        
        r += '\n'

    return r

print(pat2(3))

# pattern-3 : right angled Number Pyramid pattern
def pat3(n):
    print('Pattern - 3:\n')
    r = ''
    for i in range(1, n+1):
        for j in range(1,i+1):
            r += str(j) + ' '
        r += '\n'

    return r

print(pat3(4))

# Pattern – 4: Right-Angled Number Pyramid – II
def pat4(n):
    print('Pattern - 4:\n')
    r = ''
    for i in range(1, n+1):
        for j in range(1,i+1):
            r += str(i) + ' '
        r += '\n'

    return r

print(pat4(5))

#Pattern-5: Inverted Right Pyramid
def pat5(n):
    print('Pattern - 5:\n')
    r = ''
    for i in range(n, -1, -1):
        for j in range(0,i):
            r += '* '
        r += '\n'

    return r

print(pat5(5))

# Pattern – 6: Inverted Numbered Right Pyramid
def pat6(n):
    print('Pattern - 6:\n')
    r = ''
    for i in range(n, -1, -1):
        for j in range(1,i+1):
            r += str(j) + ' '
        r += '\n'

    return r

print(pat6(5))

# Pattern – 7: Star Pyramid
def pat7(n):
    print('Pattern - 7:\n')
    r = ''
    for i in range(n):
        for j in range(0, n-i-1):
            r += ' '
        
        for k in range(0, 2*i+1):
            r += ' * '
        
        for l in range(0, n-i-1):
            r += ' '
        r += '\n'
    return r
print(pat7(3))

# Pattern – 8: Inverted Star Pyramid
def pat8(n):
    print('Pattern - 8:\n')
    r = ''
    for i in range(1, n+1):
        for j in range(1, i+1):
            r += ' '
        
        for k in range(1, 2*n - 2*i+2):
            r += '*'
        
        for l in range(1, i+1):
            r += ' '
        r += '\n'
    return r
print(pat8(5))
