def validAnagarams(str1, str2):
    if len(str1) != len(str2):
        return False

    obj1 = {}
    for i in str1:
        if i in obj1:
            obj1[i] += 1
        else:
            obj1[i] = 1
    
    obj2 = {}
    for i in str2:
        if i in obj2:
            obj2[i] += 1
        else:
            obj2[i] = 1

    return obj1 == obj2
    
print(validAnagarams('','')) #true
print(validAnagarams('aaz','zza') )#false
print(validAnagarams('anagram','nagaram')) #true
print(validAnagarams('rat','car') )#false
print(validAnagarams('awesome','awesom') )#false
print(validAnagarams('qwerty','qewryt')) #true
print(validAnagarams('texttwisttime','timetwisttext')) #true