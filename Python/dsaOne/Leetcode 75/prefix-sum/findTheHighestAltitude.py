#https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75

def findTheHighestAltitude(gain):
    currAlt = 0
    maxAlt = 0

    for alt in gain:
        currAlt += alt
        maxAlt = max(maxAlt, currAlt)
    
    return maxAlt

print(findTheHighestAltitude([-5,1,5,0,-7]))
print(findTheHighestAltitude([-4,-3,-2,-1,4,3,2]))
