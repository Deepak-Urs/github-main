def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

print(linearSearch([1,2,35,63,7,8,9], 7))
print(linearSearch([1,2,35,63,7,8,9], 99))