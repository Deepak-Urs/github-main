def areThereDuplicates(num):
    res = {}

    for i in num:
        if i in res:
            return True
        else:
            res[i] = 1

    return False
    
    # return len(num) != len(set(num))

print(areThereDuplicates([1, 2, 3])) # false
print(areThereDuplicates([1, 2, 2])) # true 
print(areThereDuplicates(['a', 'b', 'c', 'a'])) # true 