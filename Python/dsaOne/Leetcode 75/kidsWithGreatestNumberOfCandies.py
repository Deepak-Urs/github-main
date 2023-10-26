#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

def kidsWithCandies(candies, extraCandies):
    maxCandyVal = max(candies)
    res = []
    for x in candies:
        if(x + extraCandies >= maxCandyVal):
            res.append(True)
        else:
            res.append(False)
    
    return res

print(kidsWithCandies([2,3,5,1,3], 3))
print(kidsWithCandies([4,2,1,1,2], 1))
print(kidsWithCandies([12,1,12], 10))