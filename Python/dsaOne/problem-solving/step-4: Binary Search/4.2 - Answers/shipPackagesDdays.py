def shipPackagesDdays(arr, days):
    low = max(arr)
    high = sum(arr)

    while low <= high:
        mid = (low+high)//2
        nD = findDays(arr, mid)

        if nD <= days:
            high = mid - 1
        else:
            low = mid + 1
            

    return low

def findDays(arr, capacity):
    d = 1
    ld = 0
    n = len(arr)

    for i in range(n):
        s = ld + arr[i]
        if s > capacity:
            d += 1
            ld = arr[i]
        else:
            ld += arr[i]

    return d

print(shipPackagesDdays([1,2,3,4,5,6,7,8,9,10], 5))
print(shipPackagesDdays([3,2,2,4,1,4], 3))

