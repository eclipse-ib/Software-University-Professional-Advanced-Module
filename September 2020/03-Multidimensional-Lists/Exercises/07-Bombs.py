size = int(input())

matrix = [
    [int(_) for _ in input().split()]
    for i in range(size)
]

bombs = [_.split(",") for _ in input().split()]
for bomb in bombs:
    current_bomb = matrix[int(bomb[0])][int(bomb[1])]
    c_b_row = int(bomb[0])
    c_b_col = int(bomb[1])
    damage = current_bomb
    around_squares = [
        (c_b_row-1, c_b_col -1), (c_b_row-1, c_b_col), (c_b_row-1, c_b_col +1),
        (c_b_row, c_b_col - 1), (c_b_row, c_b_col +1),
        (c_b_row + 1, c_b_col - 1), (c_b_row+1, c_b_col), (c_b_row+1, c_b_col +1)
    ]

    for square in around_squares:
        row = square[0]
        col = square[1]
        if (row < 0 or row > size-1) or (col < 0 or col > size-1):
            continue
        current_square = matrix[row][col]
        if current_square > 0:
            matrix[row][col] -= damage
    matrix[int(bomb[0])][int(bomb[1])] = 0

alive_cells = []
for i in matrix:
    for j in i:
        if j > 0:
            alive_cells.append(j)
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
print('\n'.join([' '.join(map(str, m)) for m in matrix]))
