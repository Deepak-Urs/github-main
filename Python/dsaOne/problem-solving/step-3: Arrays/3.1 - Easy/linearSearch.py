def linearSearch(arr, t):
    for i in range(len(arr)):
        if arr[i] == t:
            return i

    return None

print(linearSearch([1,2,3,4,5], 2))
print(linearSearch([2, 4, 5, 7, 9], 9))
print(linearSearch([2, 4, 5, 7, 9], 10))