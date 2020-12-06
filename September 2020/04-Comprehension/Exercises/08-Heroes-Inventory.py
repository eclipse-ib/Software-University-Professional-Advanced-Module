names = input().split(", ")
dict_names = {name: {} for name in names}

while True:
    command = input()

    if command == "End":
        break

    d_name, d_item, d_value = command.split("-")

    if d_item not in dict_names[d_name]:
        dict_names[d_name][d_item] = int(d_value)

# [print(f"{k} -> Items: {len(dict_names[k])}, Cost: {sum(dict_names[k].values())}") for k, v in dict_names.items()]
[print(f"{k} -> Items: {len(dict_names[k])}, Cost: {sum(dict_names[k].values())}") for k in dict_names]

# for k, v in dict_names.items():
#     print(f"{k} -> Items: {len(dict_names[k])}, Cost: {sum(dict_names[k].values())}")

# #Вариант с речник и списъци като values:
# names = input().split(", ")
# dict_names = {name: {} for name in names}
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     d_name, d_item, d_value = command.split("-")
#     if d_name in dict_names:
#         if d_item not in dict_names[d_name]:
#             dict_names[d_name][d_item] = int(d_value)
#
# key_sum = 0
# for key, value in dict_names.items():
#     for k, v in value.items():
#         key_sum += v
#
#     print(f"{key} -> Items: {len(value)}, Cost: {key_sum}")
