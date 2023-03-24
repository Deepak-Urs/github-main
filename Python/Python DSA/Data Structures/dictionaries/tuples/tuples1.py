t = ('1','2','3','4', '5')
# print(t)

t1 = tuple('abcde')
# print(t1)

t2 = ('1','2','3','4', '5')
# print(t2[-1])
# print(t2[1:3])
# t2[0] = '01' // cannot modify a tuple


# traversing
# for i in t2:
    # print(i)

# searching -----------
# 1 - in
print('21' in t2)

# index
print(t2.index('3'))

# iteration
def tupSearch(tup, val):
    for i in range(0, len(t2)):
        if tup[i] == val:
            return f"element is found at index {i}"
    return 'The elemenet is not found'

print(tupSearch(t2, '5'))

