#Съкратен вариант с използването на ламбда функциите в речник:
from functools import reduce


def operate(operator, *args):

    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }

    return reduce(ops[operator], args)


print(operate("+", 1, 2, 3))



# #Вариант с if проверки:
# from functools import reduce
#
#
# def operate(operator, *args):
#
#     if operator == "+":
#         return reduce(lambda a, b: a + b, args)
#     elif operator == "-":
#         return reduce(lambda a, b: a - b, args)
#     elif operator == "*":
#         return reduce(lambda a, b: a * b, args)
#     elif operator == "/":
#         return reduce(lambda a, b: a / b, args)