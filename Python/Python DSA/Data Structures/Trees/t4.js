function findMatrix(mat) {
    for(let i = 0; i < mat.length; i++)
    {
        for(let j = 0; j < mat[i].length; j++)
        {
            const after = mat[i][j];
            const before = (i - 1 >= 0 ? mat[i - 1][j] : 0) + (j - 1 >= 0 ? mat[i][j - 1] : 0) + (i > 0 && j > 0 ? mat[i - 1][j - 1] : 0);
            mat[i][j] = after - before;
        }
    }

    return mat;
}

mat = [[1,2,3], [4,5,6]]
console.log(findMatrix(mat))