
def matrix(after):
    col = len(after[0])
    row = len(after)
    bij = 0
    before = []

    for i in range(row):
        before.append([])
        for j in range(col):
            if i == 0 and j == 0:
                bij = after[0][0]
            elif i == 0:
                bij = after[0][j] - after[0][j-1]
            elif j == 0:
                bij = after[i][0] - after[i-1][0]
            else:
                bij = after[i][j] + after[i-1][j-1] - after[i][j-1] - after[i-1][j]
            before[i].append(bij)

    return before

print(matrix([[1,3], [4,10]]))