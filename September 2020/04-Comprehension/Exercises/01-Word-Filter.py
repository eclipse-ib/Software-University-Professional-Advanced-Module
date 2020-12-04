strings = input().split()

l = [i for i in strings if len(i) % 2 == 0]

for j in l:
    print(j)

# #Решение на 1 ред:
# [print(j) for j in [i for i in input().split() if len(i) % 2 == 0]]