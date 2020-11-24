# import itertools
#
# list = sum(itertools.chain(*[[1,2,3], [4,5,6]]))
# print(list)

# list = [[1,2,3], [4,5,6]]
# sum = sum([sum(i) for i in list])
# print(sum)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for value in row:
        print(value, end="")