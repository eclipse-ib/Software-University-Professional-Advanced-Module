rows, cols = [int(_) for _ in input().split()]
matrix = [
    [_ for _ in input().split()]
    for i in range(rows)
]

number_of_squares = 0

for i in range(len(matrix) - 1):
    row = matrix[i]
    for j in range(len(row) - 1):
        square = matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]
        # if matrix[i][j] == matrix[i][j + 1] and \
        #         matrix[i + 1][j] == matrix[i + 1][j + 1] and \
        #         matrix[i][j] == matrix[i + 1][j]:
        if len(set(square)) == 1:
            number_of_squares += 1

print(number_of_squares)
