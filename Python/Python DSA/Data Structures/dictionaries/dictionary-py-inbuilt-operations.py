myDict = {'name': 'Edy', 'age': 26, 'color': 'blue'}

# in --> O(n)
# print('blue' in myDict.values())

# for --> O(n)
# for key in myDict:
    # print(myDict[key])

# all
a = {1: False, 2: 'True'}
print(all(a))

#any
a = { 2: 'True', 1: False}
print(any(a))

#len
a = { 2: 'True', 1: False}
print(len(a))

#sorted
print(sorted(a, reverse=True))
