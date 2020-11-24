rows, cols = [int(_) for _ in input().split(", ")]
matrix = []

for i in range(rows):
    row = [int(el) for el in input().split()]
    matrix.append(row)

for col in zip(*matrix):
    print(sum(col))


