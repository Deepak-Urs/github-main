#https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

import collections

def equalPairs(grid):
    count = 0
    n = len(grid)

    row_counter = collections.Counter([tuple(row) for row in grid])

    for c in range(n):
        col = [grid[i][c] for i in range(n)]
        count += row_counter[tuple(col)]

    return count




print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
