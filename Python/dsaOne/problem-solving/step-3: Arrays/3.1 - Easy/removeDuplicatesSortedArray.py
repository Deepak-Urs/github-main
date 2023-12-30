#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?source=submission-noac

def removeDuplicatesSortedArray(arr):
    iidx = 1
    s = len(arr)

    for i in range(1, s):
        if arr[i] != arr[i-1]:
            arr[iidx] = arr[i]
            iidx += 1

    return iidx

print(removeDuplicatesSortedArray([1,1,2]))
print(removeDuplicatesSortedArray([0,0,1,1,1,2,2,3,3,4]))