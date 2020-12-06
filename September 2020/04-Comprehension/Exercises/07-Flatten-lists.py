#Опростен вариант без if проверка, с използването на празен split(), който изчиства всички спейсове:
line = input()
result = [el for x in line.split("|")[::-1] for el in x.split()]
print(' '.join(result))



# #Вариант с if проверка за спейсове
# line = input()
# result = [el for x in line.split("|")[::-1] for el in x.split(" ") if el != ""]
# print(' '.join(result))


# # Мой вариант със 75/100
# string = [x for x in input().split("|")[::-1]]
# numbers = [[j for j in i if j != "" and j != " "] for i in string]
#
# # numbers = []
# # for index, i in enumerate(string):
# #     numbers.append([])
# #     for j in i:
# #         if j != " ":
# #             numbers[int(index)].append(j)
#
# # numbers = numbers[::-1]
# print(' '.join([' '.join(m) for m in numbers]))