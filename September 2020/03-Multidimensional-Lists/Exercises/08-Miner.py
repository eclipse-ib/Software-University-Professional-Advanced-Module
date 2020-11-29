def s_pos(square):
    for row_i, i in enumerate(square):
        for col_j, j in enumerate(i):
            if j == "s":
                return row_i, col_j


size = int(input())
commands = input().split()
square = [
    [_ for _ in input().split()]
    for i in range(size)
]

start_pos_row, start_pos_col = s_pos(square)
current_pos_row = start_pos_row
current_pos_col = start_pos_col
coals_to_collect = sum(x.count('c') for x in square)
is_game_over = False

for command in commands:
    if command == "up":
        if (0 <= current_pos_row-1 <= size-1):
            current_pos_row -= 1
        else:
            continue

    elif command == "down":
        if (0 <= current_pos_row + 1 <= size - 1):
            current_pos_row += 1
        else:
            continue

    elif command == "left":
        if (0 <= current_pos_col - 1 <= size - 1):
            current_pos_col += - 1
        else:
            continue

    elif command == "right":
        if (0 <= current_pos_col + 1 <= size - 1):
            current_pos_col += + 1
        else:
            continue

    if square[current_pos_row][current_pos_col] == "e":
        print(f"Game over! ({current_pos_row}, {current_pos_col})")
        is_game_over = True
        break
    elif square[current_pos_row][current_pos_col] == "c":
        coals_to_collect -= 1
        square[current_pos_row][current_pos_col] = "*"
        if coals_to_collect == 0:
            print(f"You collected all coals! ({current_pos_row}, {current_pos_col})")
            break

if not is_game_over and coals_to_collect > 0:
    print(f"{coals_to_collect} coals left. ({current_pos_row}, {current_pos_col})")
