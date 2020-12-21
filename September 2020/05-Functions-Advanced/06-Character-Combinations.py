def print_comb(text, idx):
    if idx >= len(text):
        print(''.join(text))
        return
    print_comb(text, idx + 1)

    for i in range(idx + 1, len(text)):
        text[idx], text[i] = text[i], text[idx]
        print_comb(text, idx + 1)
        text[idx], text[i] = text[i], text[idx]


text = list(input())
print_comb(text, 0)

# #Решение с използването на Heap's algorithm:
# permutations = set()
#
#
# def generate(k: int, a: list ):
#     if k == 1:
#         permutations.add(''.join(a))
#     else:
#         generate(k - 1, a)
#
#         for i in range(k):
#             if k % 2 == 0:
#                 a[i], a[k-1] = a[k-1], a[i]
#             else:
#                 a[0], a[k-1] = a[k-1], a[0]
#
#             generate(k - 1, a)
#
#
# s = list(input())
# generate(len(s), s)
# print('\n'.join(list(permutations)))