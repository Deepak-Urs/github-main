# def minWindowSubStr(strg, tgt):
#     i = 0
#     j = 0
#     size = len(strg)
#     res = float('inf')
#     hm = {}
#     for c in tgt:
#         hm[c] = hm.get(c, 0) + 1
#     kL = len(hm)
#     uL = 0

#     while j < size:
#         if strg[j] in hm:
#             hm[strg[j]] -= 1

#             if hm[strg[j]] == 0:
#                 uL += 1
        
#         if uL < kL:
#             j += 1
#         elif uL == kL:
#             res = min(res, j-i+1)
#             while uL == kL:
#                 if strg[i] in hm:
#                     hm[strg[i]] += 1

#                     if hm[strg[i]] == 1:
#                         uL -= 1
#                 res = min(res, j-i+1)
                
#                 i += 1
            
#             j += 1
    
#     return res


# print(minWindowSubStr("tomptapta", "tta")) #4
# print(minWindowSubStr("pwwkew", "wwk")) # 3
# print(minWindowSubStr("aabacbebebe", "abe")) #4




# # def pickToys(strg, k):
# #     i = 0
# #     j = 0
# #     size = len(strg)
# #     res = 0
# #     hm = {}
# #     uL = 0

# #     while j < size:
# #         hm[strg[j]] = hm.get(strg[j], 0) + 1
# #         uL = len(hm)

# #         if uL < k:
# #             j += 1
# #         elif uL == k:
# #             res = max(res, j-i+1)
# #             j += 1
# #         else:
# #             while uL > k:
# #                 hm[strg[i]] = hm.get(strg[i], 0) - 1

# #                 if hm[strg[i]] == 0:
# #                     del hm[strg[i]]
# #                     uL -= 1
                
# #                 i += 1
            
# #             j += 1
    
# #     return res
    
# # print(pickToys("abacaab", 2))
# # print(pickToys("pwwkew", 3))
# # print(pickToys("aabacbebebe", 3))




# # def longestSubStrUniqueChar(strg):
# #     i = 0
# #     j = 0
# #     size = len(strg)
# #     res = 0
# #     hm = {}
# #     uL = 0

# #     while j < size:
# #         hm[strg[j]] = hm.get(strg[j], 0) + 1
# #         uL = len(hm)

# #         if j-i+1 <= uL:
# #             res = max(res, j-i+1)
# #             j += 1
# #         elif j-i+1 > uL:
# #             while j-i+1 > uL:
# #                 hm[strg[i]] = hm.get(strg[i], 0) - 1

# #                 if hm[strg[i]] == 0:
# #                     del hm[strg[i]]
# #                     uL -= 1

# #                 i += 1

# #             j += 1
    
# #     return res

# # print(longestSubStrUniqueChar("qwertyuiop"))
# # print(longestSubStrUniqueChar("pwwkew"))
# # print(longestSubStrUniqueChar("aabacbebeb"))

# # def longestSubStrKUnique(strg, k):
# #     i = 0
# #     j = 0
# #     size = len(strg)
# #     res = 0
# #     hm = {}
# #     uL = 0

# #     while j < size:
# #         hm[strg[j]] = hm.get(strg[j], 0) + 1
# #         uL = len(hm)

# #         if uL < k:
# #             j += 1
# #         elif uL == k:
# #             res = max(res, j-i+1)
# #             j += 1
# #         elif uL > k:
# #             while uL > k:
# #                 if strg[i] in hm:
# #                     hm[strg[i]] = hm.get(strg[i], 0) - 1

# #                     if hm[strg[i]] == 0:
# #                         del hm[strg[i]]
# #                         uL -= 1
                
# #                 i += 1
            
# #             j += 1
    
# #     return res

# # print(longestSubStrKUnique("qwertyuiop", 3))
# # print(longestSubStrKUnique("pwwkew", 3))
# # print(longestSubStrKUnique("aabacbebeb", 3))

