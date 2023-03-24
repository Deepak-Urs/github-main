def sameFrequency(n1, n2):
    n1, n2 = str(n1), str(n2)
    ob1, ob2 = {}, {}

    for i in n1:
        if i in ob1:
            ob1[i] += 1
        else:
            ob1[i] = 1

    for i in n2:
        if i in ob2:
            ob2[i] += 1
        else:
            ob2[i] = 1

    return ob1 == ob2

print(sameFrequency(182, 281)) #True
print(sameFrequency(34, 14)) #False
print(sameFrequency(3589578, 5879385)) #True
print(sameFrequency(22,222)) #False