#Решение с използване на функцията any():
start = int(input())
end = int(input())
numbers = [
    n
    for n in range(start, end+1)
    if any([n % m == 0 for m in range(2, 10+1)])
]
print(numbers)



#Мое решение:
# start = int(input())
# end = int(input())
#
# numbers = list(range(start, end +1))
# divisible_numbers_to = list(range(2, 10+1))
#
#
# divisible_numbers = set()
# for i in numbers:
#     for j in divisible_numbers_to:
#         if i % j == 0:
#             divisible_numbers.add(i)
#
# print(list(divisible_numbers))



#Решение на горното на един ред:
# print(list({
#     i
#     for i in list(range(int(input()), int(input())+1))
#     for j in list(range(2, 10+1)) if i % j == 0
# })
# )