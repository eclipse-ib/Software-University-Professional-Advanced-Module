countries = [i for i in input().split(", ")]
cities = [j for j in input().split(", ")]

result = list(zip(countries, cities))
print('\n'.join([' -> '.join(map(str, m)) for m in result]))