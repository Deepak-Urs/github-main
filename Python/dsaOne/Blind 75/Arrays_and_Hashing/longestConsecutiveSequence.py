#https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutiveSequence(nums):
    ns = set(nums)
    mx = 0

    for i in ns:
        l = 0
        if i-1 not in ns:
            while(i+l in ns):
                l += 1
            mx = max(mx, l)

    return mx
        
print(longestConsecutiveSequence([100,4,200,1,3,2]))
print(longestConsecutiveSequence([0,3,7,2,5,8,4,6,0,1]))