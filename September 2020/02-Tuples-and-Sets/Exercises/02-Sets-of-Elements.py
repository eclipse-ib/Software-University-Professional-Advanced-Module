n = input().split()
num_1 = int(n[0])
num_2 = int(n[1])
set_1 = set()
set_2 = set()

for i in range(1, (num_1 + num_2)+1):
    number = input()
    if i <= num_1:
        set_1.add(number)
    else:
        set_2.add(number)

final_set = set_1.intersection(set_2)
print("\n".join(final_set))