#Вариант подобен на долния, но с използването на product от itertools:
from itertools import product, chain

numbers = [n for n in input().split(", ")]
n = len(numbers)

permutations = product('-+', repeat=n)

for permutation in permutations:
    zipped = list(zip(permutation, numbers))
    expr = ''.join(chain(*zipped))
    nums = map(lambda z: int(z[1]) if z[0] == "+" else -int(z[1]), zipped)
    res = sum(nums)
    print(f"{expr}={res}")


# #Вариант подобен на долния, но с използването на sum() вмето eval():
# from itertools import permutations, chain
#
# numbers = [n for n in input().split(", ")]
# n = len(numbers)
#
# permutations = set(permutations(['-'] * n + ["+"] * n, n))
#
# for permutation in permutations:
#     zipped = list(zip(permutation, numbers))
#     expr = ''.join(chain(*zipped))
#     nums = map(lambda z: int(z[1]) if z[0] == "+" else -int(z[1]), zipped)
#     res = sum(nums)
#     print(f"{expr}={res}")


# #Вариант с permutations + chain + zip() и eval(), но при теста в джъдж дава 80/100 с един часовник,
# # и причината за него е, че се генерират прекалено много повтарящи се пермутации,
# # които после обираме вкарвайки ги в set()
#
# from itertools import permutations, chain
#
# numbers = [n for n in input().split(", ")]
# n = len(numbers)
#
# permutations = set(permutations(['-'] * n + ["+"] * n, n))
#
# for permutation in permutations:
#     expr = ''.join(chain(*zip(permutation, numbers)))
#     res = eval(expr)
#     print(f"{expr}={res}")