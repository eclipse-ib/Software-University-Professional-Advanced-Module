from mathematical_module import math_module, parser

expr = input()
res = math_module.exec(*parser.parse_expr(expr))
print(f"{res:.2f}")


# #Мое:
# from mathematical_module import math_module
#
# info = input().split()
# n1 = float(info[0])
# sign = info[1]
# n2 = int(info[2])
#
# print(math_module.mathematical_op(n1, sign, n2))


