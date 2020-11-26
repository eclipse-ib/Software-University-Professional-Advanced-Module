size = int(input())

matrix = [
    [int(el) for el in input().split()]
    for j in range(size)
]

left_diagonal = 0
right_diagonal = 0
for i in range(size):
    left_diagonal += matrix[i][i]
    right_diagonal += matrix[i][(size-1)-i]

diff = abs(left_diagonal -  right_diagonal)
print(diff)

