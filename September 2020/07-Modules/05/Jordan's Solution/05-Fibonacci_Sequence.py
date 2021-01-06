import fibonacci

while True:
    command = input()
    sequence = []
    if command.startswith("Create Sequence "):
        number = int(command.split()[-1])
        sequence = fibonacci.create_sequence(number)
        print(' '.join(str(i) for i in sequence))
    elif command.startswith("Locate "):
        search_number = int(command.split()[-1])
        try:
            pos = sequence.index(search_number)
            print(f"The number - {search_number} is at index {pos}")
        except ValueError:
            print(f"The number {search_number} is not in the sequence")

    elif command == "Stop":
        break


