def delete(stk):
    if len(stk) == 0:
        return stk
    
    k = (len(stk))//2 + 1
    remove(stk, k)
    return stk

def remove(stk, k):
    if k == 1:
        stk.pop()
        return
    
    t2 = stk.pop()
    remove(stk, k-1)
    stk.append(t2)
    
#print(delete([0,1,5,2,4,3,11,8,6]))
print(delete([0,1,5,2]))
