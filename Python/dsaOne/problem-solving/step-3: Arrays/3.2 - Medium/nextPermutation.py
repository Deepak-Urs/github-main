def nextPermuatation(nums):
    n = len(nums)
    pivot = -1

    for i in range(n-1, -1, -1):
        if nums[i] > nums[i-1]:
            pivot = i
            break
    
    if pivot == -1:
        nums.sort()
        return nums

    swap = -1
    while nums[pivot-1] >= nums[swap]:
        swap -= 1

    nums[swap], nums[pivot-1] = nums[pivot-1], nums[swap]

    nums[pivot:] = sorted(nums[pivot:])

    return nums

print(nextPermuatation([1,2,3]))
print(nextPermuatation([3,2,1]))
print(nextPermuatation([1,1,5]))

