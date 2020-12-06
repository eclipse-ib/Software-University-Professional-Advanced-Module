size = int(input())

matrix = [
    [int(el) for el in input().split(", ")]
    for i in range(size)
]

first_diagonal = [matrix[i][i] for i in range(size)]
second_diagonal = [matrix[j][(size-1)-j] for j in range(size)]

print(f"First diagonal: {', '.join([str(m) for m in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join([str(m) for m in second_diagonal])}. Sum: {sum(second_diagonal)}")

