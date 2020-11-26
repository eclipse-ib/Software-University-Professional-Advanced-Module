import itertools

rows, cols = [int(_) for _ in input().split()]
matrix = [
    [int(_) for _ in input().split()]
    for i in range(rows)
]

max_square = []
sum_square = -9999
for i in range(len(matrix) - 2):
    row = matrix[i]
    for j in range(len(row) - 2):
        square = [
            [matrix[i][j], matrix[i][j+1], matrix[i][j+2]],
            [matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2]],
            [matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]],
        ]
        current_max_square = sum(itertools.chain(*square))
        if sum_square < current_max_square:
            max_square = square
            sum_square = current_max_square

print(f"Sum = {sum_square}")
print('\n'.join([' '.join(map(str, m)) for m in max_square]))


