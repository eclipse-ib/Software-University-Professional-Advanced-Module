# Нов метод с използване на .add() - Препоръчително решение:
n = int(input())

names = set()

for _ in range(n):
    name = input()
    if name not in names:
        print(name)
        names.add(name)


#Решение на 1 ред - Непрепоръчително решение:
# print('\n'.join(set((input()) for _ in range(int(input())))))



#Решение на 3 реда - Непрепоръчително решение:
# n = int(input())
# names = [input() for _ in range(n)]
# print('\n'.join(set(names)))


# Мой метод със стари знания:
# n = int(input())
#
# names = set()
#
# for i in range(n):
#     name = input()
#     names.add(name)
#
# for j in names:
#     print(j)