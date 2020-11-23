n = int(input())

unique_elements = set()

for i in range(n):
    chemical_compounds = input().split()
    for element in chemical_compounds:
        unique_elements.add(element)

print("\n".join(unique_elements))