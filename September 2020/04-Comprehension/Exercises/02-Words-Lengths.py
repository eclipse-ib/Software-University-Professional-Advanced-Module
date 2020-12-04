strings = input().split(", ")

l = [(i, len(i)) for i in strings]

print(', '.join([' -> '.join(map(str, m)) for m in l]))

# #Решение на 1 ред:
#
# print(', '.join([' -> '.join(map(str, m)) for m in [(i, len(i)) for i in input().split(", ")]]))
