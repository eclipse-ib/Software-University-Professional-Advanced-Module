def s_pos(lair):
    for row_i, i in enumerate(lair):
        for col_j, j in enumerate(i):
            if j == "P":
                return row_i, col_j


def current_bunnies_positions(lair):
    current_b_pos = []
    for ind_b_row, b_row in enumerate(lair):
        for ind_b_col, b_col in enumerate(b_row):
            if b_col == "B":
                current_b_pos.append([ind_b_row, ind_b_col])
    return current_b_pos


def new_bunnies_positions(lair, current_bunnies_positions, current_pos_row, current_pos_col):
    for bunnie in current_bunnies_positions:
        c_b_row, c_b_col = bunnie
        next_b_pos = [[c_b_row-1, c_b_col], [c_b_row+1, c_b_col], [c_b_row, c_b_col-1], [c_b_row, c_b_col+1]]
        for next in next_b_pos:
            if (0 <= next[0] <= rows-1) and (0 <= next[1] <= cols-1):
                if (next[0] == current_pos_row and next[1] == current_pos_col) and not player_won:
                    global player_alive
                    player_alive = False
                lair[next[0]][next[1]] = "B"




rows, cols = [int(_) for _ in input().split()]
lair = [
    [_ for _ in input()]
    for i in range(rows)
]
commands = [_ for _ in input()]

start_pos_row, start_pos_col = s_pos(lair)
current_pos_row = start_pos_row
current_pos_col = start_pos_col
player_alive = True
player_won = False

for command in commands:
    if command == "U":
        next_pos_row = current_pos_row - 1
        if next_pos_row < 0 or next_pos_row > rows - 1:
            player_won = True
            lair[current_pos_row][current_pos_col] = "."
        elif lair[next_pos_row][current_pos_col] == "B":
            player_alive = False
            current_pos_row = next_pos_row

        else:
            lair[current_pos_row][current_pos_col] = "."
            current_pos_row = next_pos_row

    elif command == "D":
        next_pos_row = current_pos_row + 1
        if next_pos_row < 0 or next_pos_row > rows - 1:
            player_won = True
            lair[current_pos_row][current_pos_col] = "."
        elif lair[next_pos_row][current_pos_col] == "B":
            player_alive = False
            current_pos_row = next_pos_row

        else:
            lair[current_pos_row][current_pos_col] = "."
            current_pos_row = next_pos_row

    elif command == "L":
        next_pos_col = current_pos_col - 1
        if next_pos_col < 0 or next_pos_col > cols - 1:
            player_won = True
            lair[current_pos_row][current_pos_col] = "."
        elif lair[current_pos_row][next_pos_col] == "B":
            player_alive = False
            current_pos_col = next_pos_col

        else:
            lair[current_pos_row][current_pos_col] = "."
            current_pos_col = next_pos_col

    elif command == "R":
        next_pos_col = current_pos_col +1
        if next_pos_col < 0 or next_pos_col > cols - 1:
            player_won = True
            lair[current_pos_row][current_pos_col] = "."
        elif lair[current_pos_row][next_pos_col] == "B":
            player_alive = False
            current_pos_col = next_pos_col

        else:
            lair[current_pos_row][current_pos_col] = "."
            current_pos_col = next_pos_col

    current_bunnies_positions(lair)
    new_bunnies_positions(lair, current_bunnies_positions(lair), current_pos_row, current_pos_col)
    if not player_alive:
        break
    if player_won:
        break

print('\n'.join([''.join(map(str, m)) for m in lair]))
if not player_alive:
    print(f"dead: {current_pos_row} {current_pos_col}")
elif player_alive and player_won:
    print(f"won: {current_pos_row} {current_pos_col}")

