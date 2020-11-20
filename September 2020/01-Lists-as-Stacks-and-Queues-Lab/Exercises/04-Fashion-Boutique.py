clothes_in_the_box = [int(_)for _ in input().split()]
rack_capacity = int(input())
rack_count = 0

while len(clothes_in_the_box) > 0:
    current_rack = 0

    while current_rack <= rack_capacity:
        current_clothes = clothes_in_the_box[-1]
        if current_rack + current_clothes <= rack_capacity:
            current_rack += current_clothes
            clothes_in_the_box.pop()
            if len(clothes_in_the_box) == 0:
                rack_count += 1
                break
        else:
            rack_count += 1
            break
print(rack_count)