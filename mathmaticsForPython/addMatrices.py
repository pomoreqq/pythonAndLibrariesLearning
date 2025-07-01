a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]


def addMatrix(matrixA,matrixB):
    if len(matrixA) != len(matrixB):
        return 'matrices no same len'
    sumMatrix = list()
    for i in range(len(matrixA)):
        row = list()
        for j in range(len(matrixA[0])):
            row.append(matrixA[i][j] + matrixB[i][j])
        sumMatrix.append(row)
    return sumMatrix

print(addMatrix(a,b))