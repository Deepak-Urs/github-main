def EqualSumPartition(arr, sm):
    r = len(arr) + 1
    c = sm + 1

    # initialization
    res = [[] for i in range(r)]
    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0 or j == 0: res[i].append(True)
            elif i == 0: res[i].append(False)
            else: res[i].append(None)

    # result calculation
    for i in range(r):
        for j in range(c):
            if arr[i-1] <= j:
                res[i][j] = res[i-1][j-arr[i-1]] or res[i-1][j]
            elif arr[i-1] > j:
                res[i][j] = res[i-1][j]

    return res[i][j]


def main(arr):
    sm = sum(arr)

    if sm%2 != 0:
        return False
    elif sm%2 == 0:
        return EqualSumPartition(arr, sm//2)
    
print(main([2,5,7,6,10]))