integers = [1,2,3,4]
# print(integers)

mixList = [1, 'a', True, [2, 'b', False]]
# print(mixList)

# accessing or traversing in a list
shoppingList = ['Milk', 'Cheese', 'Butter']

print(shoppingList[0])
print('Milk' in shoppingList)
print(shoppingList[-2])

for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"

print(shoppingList)

empty = []
for i in empty:
    print('I am empty')