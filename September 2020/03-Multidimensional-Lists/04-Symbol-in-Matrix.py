#Вариант с използването на функция:
# def find_in_matrix(matrix, searching_char):
#     for i, row in enumerate(matrix):
#         for j, value in enumerate(row):
#             if value == searching_char:
#                 return i, j
#
#
# n = int(input())
# matrix = [list(input()) for el in range(n)]
# searching_char = input()
#
# pos = find_in_matrix(matrix, searching_char)
#
# if pos:
#     print(pos)
# else:
#     print(f"{searching_char} does not occur in the matrix")

#Boolean вариант:
# size = int(input())
#
# matrix = [
#     [el for el in input()]
#     for i in range(size)
# ]
#
# searching_char = input()
# coincidence = ()
#
# for i in range(size):
#     for j in range(size):
#         if matrix[i][j] == searching_char:
#             coincidence = i, j
#
# if coincidence:
#     print(coincidence)
# else:
#     print(f"{searching_char} does not occur in the matrix")

#Вариант с exit():
# size = int(input())
#
# matrix = [
#     [el for el in input()]
#     for i in range(size)
# ]
#
# searching_char = input()
#
#
# for i in range(size):
#     for j in range(size):
#         if matrix[i][j] == searching_char:
#             print(f"({i}, {j})")
#             exit()
#
# print(f"{searching_char} does not occur in the matrix")