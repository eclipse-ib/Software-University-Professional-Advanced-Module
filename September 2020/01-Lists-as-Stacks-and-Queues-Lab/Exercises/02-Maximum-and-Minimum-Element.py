n = int(input())

stack = []

for _ in range(n):
    command = input()

    if command.startswith("1"):
        number = int(command.split()[1])
        if 0 <= number <= 109:
            stack.append(number)

    elif command.startswith("2"):
        if len(stack) == 0:
            continue
        stack.pop()

    elif command.startswith("3") and len(stack) > 0:
        print(max(stack))

    elif command.startswith("4") and len(stack) > 0:
        print(min(stack))

print(", ".join(reversed([str(i) for i in stack])))