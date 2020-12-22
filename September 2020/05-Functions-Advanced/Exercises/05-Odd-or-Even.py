command = input()
list_of_numbers = [int(i) for i in input().split()]
result = 0

if command == "Odd":
    # odd_numbers = list(filter(lambda x: x % 2 != 0, list_of_numbers))
    # print(sum(odd_numbers) * len(list_of_numbers))
    result = sum(list(filter(lambda x: x % 2 != 0, list_of_numbers))) * len(list_of_numbers)
elif command == "Even":
    # even_numbers = list(filter(lambda x: x % 2 == 0, list_of_numbers))
    # print(sum(even_numbers) * len(list_of_numbers))
    result = sum(list(filter(lambda x: x % 2 == 0, list_of_numbers))) * len(list_of_numbers)
print(result)