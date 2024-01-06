def firstOccurrence(nums, target):
    low = 0
    high = len(nums) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if nums[mid] == target:
            first = mid
            # look for smaller index on the left
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1  # look on the right
        else:
            high = mid - 1  # look on the left

    return first


def lastOccurrence(nums, target):
    low = 0
    high = len(nums) - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if nums[mid] == target:
            last = mid
            # look for larger index on the right
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1  # look on the right
        else:
            high = mid - 1  # look on the left

    return last


def findFirstLastOccurence(nums, target):
    first = firstOccurrence(nums, target)
    if first == -1:
        return (-1, -1)
    last = lastOccurrence(nums, target)
    return (first, last)


print(findFirstLastOccurence([5,7,7,8,8,10], 8))
print(findFirstLastOccurence([5,7,7,8,8,10], 6))
print(findFirstLastOccurence([], 0))