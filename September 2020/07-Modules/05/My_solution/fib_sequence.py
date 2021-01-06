def sequence(count):
    first_number = 0
    second_number = 1
    list_sequence = [0, 1]
    for i in range(count-2):
        next_number = first_number+second_number
        list_sequence.append(next_number)
        first_number = second_number
        second_number = next_number
    return list_sequence


def locate(number, count):
    numbers = sequence(count)
    if number in numbers:
        index = list(numbers).index(number)
        print(f"The number - {number} is at index {index}")
    else:
        print(f"The number {number} is not in the sequence")
