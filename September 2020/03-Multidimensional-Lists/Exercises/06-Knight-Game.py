#От лекциите:
def is_valid(pos, size):
    row = pos[0]
    col = pos[1]
    return 0 <= row < size and 0 <= col < size


def get_killed_knights(row, col, size, board):
    killed_knights = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        current_pos = [row + rows[i], col + cols[i]]
        if is_valid(current_pos, size) and board[current_pos[0]][current_pos[1]] == "K":
            killed_knights += 1
    return killed_knights


n = int(input())
board = []
total_kills = 0

for _ in range(n):
    board.append([x for x in input()])

while True:
    most_kills = 0
    to_kill = []

    for row in range(n):
        for col in range(n):
            if board[row][col] == "K":
                killed_knights = get_killed_knights(row, col, n, board)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_kill = [row, col]
    if most_kills == 0:
        break

    to_kill_row = to_kill[0]
    to_kill_col = to_kill[1]
    board[to_kill_row][to_kill_col] = "0"
    total_kills += 1

print(total_kills)

# Опит за мой вариант-неуспешен
# size = int(input())
# matrix = [
#     [_ for _ in input()]
#     for s in range(size)
# ]
#
# max_attacked_knights = 0
# knight = ""
# removed_knight = 0
# for index, val in enumerate(matrix):
#     for ind, j in enumerate(val):
#         current_count_attacked_knights = 0
#         knight_moves = {
#             "ups": [
#                 matrix[index - 1][ind - 2], matrix[index - 1][ind + 2], matrix[index - 2][ind - 1], matrix[index - 2][ind + 1]
#             ],
#             "downs": [
#                 matrix[index + 1][ind - 2], matrix[index + 1][ind + 2], matrix[index + 2][ind - 1], matrix[index + 2][ind + 1]
#             ],
#             "lefts": [
#                 matrix[index + 2][ind - 1], matrix[index - 2][ind - 1], matrix[index + 1][ind - 2], matrix[index - 1][ind - 2]
#             ],
#             "rights": [
#                 matrix[index + 2][ind + 1], matrix[index - 2][ind + 1], matrix[index + 1][ind + 2], matrix[index - 1][ind + 2]
#             ],
#         }
#         for key, value in knight_moves.items():
#             for v in value:
#                 print(v)
#                 if v and v == "K":
#                     current_count_attacked_knights += 1
#         if current_count_attacked_knights > max_attacked_knights:
#             max_attacked_knights = current_count_attacked_knights
#             knight = matrix[index][ind]
#             matrix[index][ind] = "0"
#             removed_knight += 1
# print(removed_knight)