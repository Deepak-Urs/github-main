#https://www.codingninjas.com/studio/problems/sorted-array_6613259?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

def sortedArray(a, b):
    # solution-1
    #freq = {}

    #for i in a:
    #    if i in freq:
    #        freq[i] += 1
    #    else:
    #        freq[i] = 1
    
    #for i in b:
    #    if i in freq:
    #        freq[i] += 1
    #    else:
    #        freq[i] = 1

    #r = []
    #for i in freq:
    #    r.append(i)

    #return r

    # solution-2
    r = a + b
    s = set(r)

    return list(s)

print(sortedArray([1, 2, 3, 4, 6], [2, 3, 5]))
print(sortedArray([1, 2, 3, 3], [2,2,4]))
