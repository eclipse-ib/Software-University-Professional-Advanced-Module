#Вариант само с for цикъл:
from itertools import combinations

people = input().split(", ")
chairs = int(input())

combinations = combinations(people, chairs)

for combination in combinations:
    print(', '.join(combination))

# #Вариант с функция:
# from itertools import combinations
#
#
# def test(people, chairs):
#     people_comb = list(combinations(people, chairs))
#     return people_comb
#
#
# # for i in test([name for name in input().split(", ")], int(input())):
# #     print(', '.join(i))
#
#
# print('\n'.join([', '.join(i) for i in test([name for name in input().split(", ")], int(input()))]))