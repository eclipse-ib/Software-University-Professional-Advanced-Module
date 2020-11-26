rows, cols = [int(_) for _ in input().split()]
matrix = [
    [_ for _ in input().split()]
    for i in range(rows)
]

while True:
    command = input().split()
    if command[0] == "END":
        break

    if command[0] == "swap" and len(command) == 5:
        valid_command = (
            (0 <= int(command[1]) <= rows and 0 <= int(command[3]) <= rows) and
            (0 <= int(command[2]) <= cols and 0 <= int(command[4]) <= cols)
        )
        if valid_command:
            row_1 = int(command[1])
            col_1 = int(command[2])
            row_2 = int(command[3])
            col_2 = int(command[4])
            matrix[row_1][col_1], matrix[row_2][col_2]  = matrix[row_2][col_2], matrix[row_1][col_1]
            print('\n'.join([' '.join(m) for m in matrix]))
            continue
    print("Invalid input!")
