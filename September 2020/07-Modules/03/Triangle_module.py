def triangle(n):
    for row in range(n+1):
        print(*[i for i in range(1, row+1)])
    for row in range(n, 0, -1):
        print(*[i for i in range(1, row)])

# ламерски вариант:
# def triangle(n):
#     for row in range(1, n+1):
#         count = 0
#         print()
#         for col in range(row):
#             print(1 + count, end=' ')
#             count += 1
#
#     for row2 in range(n-1, 0, -1):
#         count2 = 0
#         print()
#         for col in range(row2):
#             print(1 + count2, end=' ')
#             count2 += 1