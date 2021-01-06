import fib_sequence


while True:
    commands = input().split()
    command = commands[0]

    if command == "Stop":
        break

    if command == "Create":
        count = int(commands[2])
        print(' '.join(str(i) for i in fib_sequence.sequence(count)))

    elif command == "Locate":
        number = int(commands[1])
        fib_sequence.locate(number, count)