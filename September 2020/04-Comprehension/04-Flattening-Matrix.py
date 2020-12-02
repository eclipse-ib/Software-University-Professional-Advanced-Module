#Решение с for цикли:
size = int(input())
l = []
for _ in range(size):
    for n in input().split(", "):
        l.append(int(n))
print(l)



# #Решение с компрехеншъни на няколко реда:
# size = int(input())
#
# matrix = [[int(j) for j in input().split(", ")] for i in range(size)]
# flatten_matrix = [num for sublist in matrix for num in sublist]
#
# print(flatten_matrix)



# # #Решение на горното на един ред с 2 for-a:
# print([int(n) for _ in range(int(input())) for n in input().split(", ")])



# #Решение на горното на един ред с 3 for-a:
# print([num for sublist in [[int(j) for j in input().split(", ")] for i in range(int(input()))]\
#        for num in sublist])