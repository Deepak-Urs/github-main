def longestConsecutiveSequence(nums):
    ns = set(nums)
    mc = 0

    for i in ns:
        if i - 1 not in ns:
            c = 0
            while i + c in ns:
                c += 1
            mc = max(c, mc)

    return mc

print(longestConsecutiveSequence([5, 8, 3, 2, 1, 4]))
print(longestConsecutiveSequence([15,6,2,1,16,4,2,29,9,12,8,5,14,21,8,12,17,16,6,26,3]))

