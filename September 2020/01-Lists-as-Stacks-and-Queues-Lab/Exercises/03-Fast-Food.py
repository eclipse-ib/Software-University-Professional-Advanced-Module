from collections import deque

quantity_of_the_food = int(input())
orders = deque([int(_) for _ in input().split()])

print(max(orders))

while len(orders) > 0:
    current_order = orders[0]
    if current_order > quantity_of_the_food:
        print(f"Orders left: {' '.join([str(_) for _ in orders])}")
        exit()

    quantity_of_the_food -= orders.popleft()

print("Orders complete")