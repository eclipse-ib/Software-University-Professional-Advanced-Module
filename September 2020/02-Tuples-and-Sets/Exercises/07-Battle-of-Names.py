n = int(input())

even_names = set()
odd_names = set()

for i in range(1, n+1):
    name = input()
    current_ascii_sum = 0
    for char in name:
        current_ascii_sum += ord(char)

    current_ascii_sum = current_ascii_sum // i

    if current_ascii_sum % 2 == 0:
        even_names.add(current_ascii_sum)
    else:
        odd_names.add(current_ascii_sum)

result = ""
if sum(even_names) == sum(odd_names):
    result = odd_names.union(even_names)

elif sum(even_names) < sum(odd_names):
    result = odd_names.difference(even_names)

elif sum(even_names) > sum(odd_names):
    result = odd_names.symmetric_difference(even_names)

print(", ".join(str(_) for _ in result))
