import itertools
#Пример със съкратено решение с компрехеншъни и използване нa itertools + chain:
rows, columns = [int(element) for element in input().split(", ")]

matrix = [[int(_) for _ in input().split(", ")] for i in range(rows)]
sum_matrix = sum(itertools.chain(*matrix))
print(sum_matrix)
print(matrix)

#Това може да бъде направено лесно и кратко с компрехеншън
# size = input().split(", ")
# rows = int(size[0])
# columns = int(size[1])
# rows, columns = [int(element) for element in input().split(", ")]
#
# matrix = []
# sum_matrix = 0
# for i in range(rows):
#     command = input().split(", ")
#     matrix.append([])
#     for j in command:
#         matrix[i].append(int(j))
#         sum_matrix += int(j)
#
# print(sum_matrix)
# print(matrix)

