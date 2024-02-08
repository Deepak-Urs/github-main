def reverse(stk):
    if len(stk) == 1:
        return stk

    t = stk.pop()
    reverse(stk)

    insert(stk,t)

    return stk

def insert(stk, t):
    if len(stk) == 0:
        stk.append(t)
        return
    
    t2 = stk.pop()
    insert(stk, t)
    stk.append(t2)

print(reverse([1,2,3,4,5]))