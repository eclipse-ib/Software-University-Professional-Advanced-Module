string = tuple(float(_) for _ in input().split())

dict_nums = {}

for i in string:
    if i not in dict_nums:
        dict_nums[i] = 1
    else:
        dict_nums[i] += 1

[print(f"{key} - {value} times") for key, value in dict_nums.items()]