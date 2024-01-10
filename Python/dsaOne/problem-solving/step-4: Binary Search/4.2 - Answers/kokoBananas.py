#https://leetcode.com/problems/koko-eating-bananas/description/

def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) / 2
        if canEatAll(piles, mid, h):
            right = mid
        else:
            left = mid + 1

    return left

def canEatAll(piles, speed, h):
    time = 0
    for pile in piles:
        time += (pile - 1) / speed + 1
        if time > h:
            return False
    return True


print(minEatingSpeed([3,6,7,11], 8))
print(minEatingSpeed([30,11,23,4,20], 5))
print(minEatingSpeed([30,11,23,4,20], 6))
