from collections import deque

rows, cols = [int(_) for _ in input().split()]
string = input()

matrix = [[0 for j in range(cols)] for i in range(rows)]
# matrix = []
#
# for i in range(rows):
#     matrix.append([])
#     for j in range(cols):
#         matrix[i].append(0)

key_word = deque(string)
count = 0
for i in range(rows):
    for j in range(cols):
        if not key_word:
            key_word = deque(string)

        matrix[i][j] = key_word.popleft()

    if count % 2 != 0:
        matrix[i] = matrix[i][::-1]
    count += 1

print('\n'.join([''.join(map(str, m)) for m in matrix]))
