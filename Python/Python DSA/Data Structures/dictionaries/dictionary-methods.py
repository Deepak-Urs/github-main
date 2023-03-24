
myDict = {'name': 'Edy', 'age': 26, 'color': 'blue'}

#clear()
# myDict.clear()
print(myDict)


#copy()
dict = myDict.copy()
print(myDict)
print(dict)

myDict = {'name': 'Edy', 'age': 26, 'color': 'blue'}

newDict = {}.fromkeys([1,2,3], 0)
print(newDict)

print(myDict.get('age', 27))


print(myDict.items())

print(myDict.popitem())
print(myDict)


myDict = {'name': 'Edy', 'age': 26, 'color': 'blue'}
print(myDict.setdefault('name2', 'added'))
print(myDict)

print(myDict.pop('nam3', 'removed'))

print(myDict.values())

n2 = {'test': 'test'}
print(myDict.update(n2))
print(myDict)