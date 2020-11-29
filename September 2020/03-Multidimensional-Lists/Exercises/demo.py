# list = [['foobar', 'a', 'b'], ['x', 'c'], ['y', 'd', 'e', 'foobar'], ['z', 'f']]
# x = sum(x.count('foobar') for x in list)
# print(x)


a = [[1, 2], [3, "s"], [5, 6]]

x = [x for x in a if "s" in x][0]

print(f'The index is (%d,%d)' % (a.index(x), x.index("s")))
