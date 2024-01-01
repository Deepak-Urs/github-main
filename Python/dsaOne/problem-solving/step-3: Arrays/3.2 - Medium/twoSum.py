def twoSum(arr, s):
    hm = {}
    for i in range(0, len(arr)):
        another = s - arr[i]

        if another in hm:
            return [hm[another], i]
        else:
            hm[arr[i]] = i
    
    return None

print(twoSum([2,6,5,8,11], 14))
print(twoSum([2,6,5,8,11], 15))