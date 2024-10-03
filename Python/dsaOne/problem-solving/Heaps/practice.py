# from heapq import heappush, heappop

# def k_closest_points_to_origin(arr, k):
#     maxH = []

#     for i in arr:
#         heappush(maxH, [-(i[0]*i[0] + i[1]*i[1]), i])
#         if len(maxH) > k:
#             heappop(maxH)
    
#     while k > 0:
#         print(heappop(maxH)[1])
#         k -= 1

# k_closest_points_to_origin([[1,3],[-2,2], [5,8],[0,1]], 2)
# # def freq_sort(nums):
# #     hm = {}
# #     minH = []
# #     for i in nums:
# #         hm[i] = hm.get(0, i) + 1
    
# #     for k in hm:
# #         heappush(minH, [-hm[k], k])
    
# #     for j in range(len(minH)-1, -1, -1):
# #         print(minH[j][1])

# # freq_sort([1,2,1,4,2,1,3])
    
# # def top_k_freq_ele(nums, k):
# #     hm = {}
# #     minH = []

# #     for i in nums:
# #         hm[i] = hm.get(0, i) + 1

# #     for i in hm:
# #         heappush(minH, [-hm[i], i])
# #         if len(minH) > k:
# #             heappop(minH)
    
# #     for i in range(len(minH)-1, -1, -1):
# #         print(minH[i][1])

# # top_k_freq_ele([1,1,1,2,4,2,3], 2)

# # def k_closest_numbers(nums, k, x):
# #     minH = []

# #     for i in nums:
# #         heappush(minH, [-abs(i-x), i])
# #         if len(minH) > k:
# #             heappop(minH)
    
# #     while len(minH) > 0:
# #         val = heappop(minH)
# #         print(val[1])

# # k_closest_numbers([2,3,6,7,8,90], 3, 7)


# # def sort_k_sorted_arr(nums, k):
# #     minH = []
# #     res = []
    
# #     for i in nums:
# #         heappush(minH, i)
# #         if len(minH) > k:
# #             res.append(heappop(minH))
    
# #     while len(minH) > 0:
# #         res.append(heappop(minH))
    
# #     return res

# # print(sort_k_sorted_arr([6,5,3,2,8,10,9], 3))

# # def print_k_largest_elements(nums, k):
# #     maxH = []
# #     for i in nums:
# #         heappush(maxH, i)
# #         if len(maxH) > k:
# #             heappop(maxH)
    
# #     return maxH

# # print(print_k_largest_elements([7,10,4,3,20,15], 3))




# # def kth_smallest_ele(nums, k):
# #     minH = []
# #     for i in nums:
# #         heappush(minH, -i)
# #         if len(minH) > k:
# #             heappop(minH)
    
# #     return -minH[0]

# # print(kth_smallest_ele([7,10,4,3,20,15], 3))