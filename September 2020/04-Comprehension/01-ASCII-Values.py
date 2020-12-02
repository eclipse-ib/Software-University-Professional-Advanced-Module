# string = input().split(", ")
#
# dict = {}
#
# for char in string:
#     dict[char] = ord(char)
# print()

new_dict = {char: ord(char) for char in input().split(", ")}
print(new_dict)
