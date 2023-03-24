myDict = {'name': 'Edy', 'age': 26}
myDict['address'] = 'London'
# print(myDict)

def traversDict(dict):
    for key in dict:
        print(key, dict[key])

# traversDict(myDict)

def searchDict(dict, val):
    for key in dict:
        if dict[key] == val:
            return key, val
    return 'Value not found'

# print(searchDict(myDict, 'Edy'))

# pop


#1
myDict = {'name': 'Edy', 'age': 26}
myDict.pop('name')
# print(myDict)


#2
myDict = {'name': 'Edy', 'age': 26}
# print(myDict.popitem())
# print(myDict)

#3
myDict = {'name': 'Edy', 'age': 26}
myDict.clear()
# print(myDict)


#3
myDict = {'name': 'Edy', 'age': 26}
del myDict['age']
print(myDict)