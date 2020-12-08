categories = {l: {} for l in input().split(", ")}
n = int(input())
for _ in range(n):
    command = input().split(" - ", maxsplit=3)
    category = command[0]
    item = command[1]
    item_info = command[2].split(";")

    quantity = item_info[0].split(':')
    n_quantity = int(quantity[1])

    quality = item_info[1].split(':')
    n_quality = int(quality[1])

    if item not in categories[category]:
        categories[category][item] = [n_quantity, n_quality]

sum_items = 0
average_quality = []
for key, values in categories.items():
    for k, v in values.items():
        sum_items += v[0]
        average_quality.append(v[1])
print(f"Count of items: {sum_items}")
print(f"Average quality: {(sum(average_quality) / len(categories)):.2f}")

# for key, values in categories.items():
#     print(f"{key} -> {', '.join([i for i in values])}")
[print(f"{key} -> {', '.join([i for i in values])}") for key, values in categories.items()]
