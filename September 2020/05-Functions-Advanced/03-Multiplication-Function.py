#Варинат с използването на prod от math:
import math
multiply = lambda *args: math.prod(args)
print(multiply(1, 4, 5))


# #Вариант с използването на reduce() в обикновенна функция, както и на mul от operator:
# from operator import mul
# from functools import reduce
#
#
# def multiply(*args):
#     return reduce(mul, args)
#
# print(multiply(1, 4, 5))


# #Вариант с използването на reduce() в обикновенна функция:
# from functools import reduce
#
#
# def multiply(*args):
#     return reduce(lambda a, b: a * b, args)
#
# print(multiply(1, 4, 5))


# # Вариант с използването на recude() в ламбда функция:
# from functools import reduce
#
# multiply = lambda *args: reduce(lambda a, b: a * b, args)
#
# print(multiply(1, 4, 5))


# #Вариант с използването на фукция и цикъл в нея:
# def multiply(*args):
#     result = 1
#     for i in args:
#         result *= i
#     return result
#
# print(multiply(2, 0, 1000, 5000))
