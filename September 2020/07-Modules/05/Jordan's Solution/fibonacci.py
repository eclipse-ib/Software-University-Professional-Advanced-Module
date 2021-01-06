def create_sequence(number):
    assert number >= 1, f'The number must be >0'

    if number == 1:
        sequence = [0]
    elif number == 2:
        sequence = [0, 1]
    else:
        sequence = [0, 1]
        for _ in range(0, number-2):
            sequence.append(sequence[-1] + sequence[-2])
    return sequence
