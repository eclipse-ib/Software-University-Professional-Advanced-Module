# size = int(input())
#
# matrix = [[int(j) for j in input().split(", ")] for i in range(size)]
#
#
# even_matrix = [[col for col in row if col % 2 == 0] for row in matrix]
# print(even_matrix)


#Решение на 1 ред
# print([
#     [col for col in row if col % 2 == 0]
#     for row in [[int(j) for j in input().split(", ")]
#                 for i in range(int(input()))]
# ]
# )

#По-кратко решение на 1 ред:

matrix =[
    [
        int(j)
        for j in input().split(", ")
        if int(j) % 2 == 0
    ]
    for _ in range(int(input()))
]
