# nums = [1, 2, 3, 4, 5, 6]
# filtered = [x % 2 == 0 for x in nums]
#
# print(filtered)

# info = [("Peter", 22), ("Amy", 18), ("George", 35)]
# dict = dict(info)
# print(dict)

vowels = {'a', 'o', 'u', 'e', 'i'}
vowels = {'a', 'o', 'u', 'e', 'i'} | {c.upper() for c in vowels.copy()}
print(vowels)