#Правилното решение с пълен компрехеншън:
rows, cols = [int(x) for x in input().split()]

matrix = [
    [f"{chr(row)}{chr(row+col)}{chr(row)}" for col in range(cols)]
    for row in range(97, (97+rows))

]

print('\n'.join([' '.join(map(str, m)) for m in matrix]))


# #Правилното решение без пълен компрехеншън:
# rows, cols = [int(x) for x in input().split()]
#
# for row in range(97, (97+rows)):
#     if row != 0:
#         print()
#     for col in range(cols):
#         print(f"{chr(row)}{chr(row+col)}{chr(row)}", end=" ")

# # Някакъв мой начин:
# r, c = [int(x) for x in input().split()]
#
#
# matrix = []
# for _ in range(r):
#     if _ != 0:
#         print()
#
#     for i in range(c):
#         first_letter = 97 + _
#         print(chr(first_letter), end="")
#         second_letter = first_letter + i
#         print(chr(second_letter), end="")
#         print(chr(first_letter), end=" ")
