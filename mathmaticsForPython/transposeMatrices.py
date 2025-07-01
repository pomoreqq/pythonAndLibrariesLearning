matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]


#return [list(row) for row in zip(*matrix)]