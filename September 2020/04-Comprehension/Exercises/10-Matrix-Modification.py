rows = int(input())
matrix = [[int(_) for _ in input().split()] for i in range(rows)]

while True:
    commands = input().split()
    command = commands[0]
    if command == "END":
        break
    row = int(commands[1])
    col = int(commands[2])
    value = int(commands[3])
    if 0 > row or row > rows-1 or 0 > col or col > rows-1:
        print(f"Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value

    elif command == "Subtract":
        matrix[row][col] -= value

print('\n'.join([' '.join(map(str, m)) for m in matrix]))