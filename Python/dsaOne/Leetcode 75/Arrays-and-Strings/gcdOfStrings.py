#https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
from math import gcd

def gcdOfStrings(src, tgt):
    if(not (src + tgt == tgt + src)):
        return ""
    
    return src[:gcd(len(src), len(tgt))]

print(gcdOfStrings("ABCABC", "ABC"))
print(gcdOfStrings("ABABAB", "ABAB"))
print(gcdOfStrings("LEET", "CODE"))