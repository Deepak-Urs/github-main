#update/insert list

myList = [1,2,3,4,5]
# print(myList)

myList[2] = 9
# print(myList)

# insert()
# print(myList)
myList.insert(4, 11)
# print(myList)

myList.append('append-value')
# print(myList)

newList = [10,20,30]
myList.extend(newList)
# print(myList)

myList = ['a', 'b', 'c', 'd', 'e']
# myList[0:2] = ['x', 'y']
# print(myList)
# print(myList[0:2])

print(myList.pop(1))
# print(myList)

del myList[1]
# print(myList)

print('del range')
myList = ['a', 'b', 'c', 'd', 'e']
del myList[4:4]
# print(myList)

myList.remove('e')
# print(myList)

myList = [1,2,3,4,5,6,7,8,9]

def searchInList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return "The value doesn't exist in the list"

print(searchInList(myList, 9))
