numbers_list = [int(i) for i in input().split()]
even_numbers = list(filter((lambda x: x % 2 == 0), numbers_list))
print(even_numbers)