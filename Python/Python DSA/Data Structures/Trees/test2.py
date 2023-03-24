class Solution:
    def findBeforematrix(self, afterMatrix):
        m = len(afterMatrix)
        n = len(afterMatrix[0])
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i-1 >= 0 and j-1 >= 0:
                    afterMatrix[i][j] = afterMatrix[i][j] - afterMatrix[i-1][j] - afterMatrix[i][j-1] + afterMatrix[i-1][j-1]
                elif j-1 >= 0 and i-1 < 0:
                    afterMatrix[i][j] -= afterMatrix[i][j-1]
                elif i-1 >= 0 and j-1 < 0:
                    afterMatrix[i][j] -= afterMatrix[i-1][j]
        
        return afterMatrix
    
    
s = Solution()
afterMatrix = [[1,2,3], [4,5,6]]
result = s.findBeforematrix(afterMatrix)
print(result)