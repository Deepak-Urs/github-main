#def insert(arr, t):
#     if len(arr) == 0:
#         arr.append(t)
#         return
    
#     t2 = arr.pop()
#     insert(arr, t)
#     arr.append(t2)

# def revArr(arr):
#     if len(arr) == 1:
#         return
    
#     t = arr.pop()
#     revArr(arr)
#     insert(arr, t)

#     return arr

# print(revArr([1,2,3,4,5]))


# # def insert(arr, t):
# #     if len(arr) == 0 or arr[len(arr)-1] <= t:
# #         arr.append(t)
# #         return
    
# #     t2 = arr.pop()
# #     insert(arr, t)
# #     arr.append(t2)


# # def sort(arr):
# #     if len(arr) == 1:
# #         return arr
    
# #     t = arr.pop()
# #     sort(arr)

# #     insert(arr, t)
# #     return arr

# # print(sort([0,1,5,2]))



# # def printNto1(num):
# #     if num == 0:
# #         return
    
# #     print(num)

# #     printNto1(num-1)

# # printNto1(7)



# # def print1toN(num):
# #     if num == 0: # B
# #         return
    
# #     print1toN(num-1) # H

# #     print(num) #I

# # print1toN(7)

