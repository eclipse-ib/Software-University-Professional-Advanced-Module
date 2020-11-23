n = int(input())

list_l_i = []

for i in range(n):
    current_range_1 = set()
    current_range_2 = set()

    ranges = input().split("-")
    r_1, r_2 = ranges[0].split(",")
    r_3, r_4 = ranges[1].split(",")
    for cr1 in range(int(r_1), int(r_2)+1):
        current_range_1.add(cr1)

    for cr2 in range(int(r_3), int(r_4)+1):
        current_range_2.add(cr2)

    current_intersection = current_range_1.intersection(current_range_2)
    if len(current_intersection) > len(list_l_i):
        list_l_i = current_intersection

print(f"Longest intersection is {list(list_l_i)} with length {len(list_l_i)}")


