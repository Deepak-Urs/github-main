#https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75

def uniqueNumOccurances(nums):
    hm = {}
    ca = []

    for i in nums:
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 1
    
    for i in hm:
        ca.append(hm[i])

    return len(ca) == len(set(ca))

print(uniqueNumOccurances([1,2,2,1,1,3]))
print(uniqueNumOccurances([1,2]))
print(uniqueNumOccurances([-3,0,1,-3,1,1,1,-3,10,0]))

