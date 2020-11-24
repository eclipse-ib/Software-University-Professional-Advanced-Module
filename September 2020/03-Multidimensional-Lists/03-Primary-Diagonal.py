#Съкратен Вариант с комрехеншън:
size = int(input())

matrix = [
    [int(el) for el in input().split()]
    for i in range(size)
]
current_sum = sum([matrix[i][i] for i in range(size)])

print(current_sum)

#Вариант с range:
# size = int(input())
#
# matrix = [
#     [int(el) for el in input().split()]
#     for i in range(size)
# ]
#
# current_sum = 0
# for i in range(size):
#     current_sum += matrix[i][i]
#
# print(current_sum)


# Вариант с ожхождане на матрицата:
# size = int(input())
#
# matrix = [
#     [int(el) for el in input().split()]
#     for i in range(size)
# ]
#
# index = 0
# current_sum = 0
# for j in matrix:
#     current_sum += j[index]
#     index += 1
# print(current_sum)
