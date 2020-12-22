def even_odd(*args):
    numbers_of_args = args[:-1]
    command = args[-1]
    if command == "even":
        return list(filter(lambda x: x % 2 == 0, numbers_of_args))
    return list(filter(lambda x: x % 2 != 0, numbers_of_args))


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
