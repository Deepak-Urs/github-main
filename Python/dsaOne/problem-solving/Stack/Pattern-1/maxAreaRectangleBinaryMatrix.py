from maxAreaHistogram import maxAreaHistogram

# 0 1 1 0
# 1 1 1 1
# 1 1 1 1
# 1 1 0 0

def maxAreaRectangleBinaryMatrix(mat):
    nR = len(mat)
    mC = len(mat[0])
    mI = []
    resArea = 0

    for jx in range(mC): 
        mI.append(mat[0][jx])
    resArea = max(resArea, maxAreaHistogram(mI))

    for r in range(1, nR):
        for c in range(mC):
            if r > 0  and mat[r][c] == 0:
                mI[c] = 0
            else:
                mI[c] = mI[c] + mat[r][c]
                
        resArea = max(resArea, maxAreaHistogram(mI))

    return resArea

print(maxAreaRectangleBinaryMatrix([[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]))