string = input()
count_symbols = {}

for char in string:
    if char not in count_symbols:
        count_symbols[char] = 1
    else:
        count_symbols[char] += 1

sorted_symbols = sorted(count_symbols.items())
for key, value in sorted_symbols:
    print(f"{key}: {value} time/s")