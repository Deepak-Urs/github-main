#https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

def canPlaceFlowers(flowerbed, n):
    f = [0] + flowerbed + [0]

    for i in range(1, len(f)-1):
        if(f[i-1] == 0 and f[i] == 0 and f[i+1] == 0):
            f[i] = 1
            n -= 1
    
    return n <= 0

print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1], 2))