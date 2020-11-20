from collections import deque

cups = deque(int(_) for _ in input().split())
bottles = deque(int(_) for _ in input().split())

wasted_water = 0

while True:

    if len(cups) == 0:
        print(f"Bottles: {' '.join(str(_) for _ in bottles)}")
        break

    if len(bottles) == 0:
        print(f"Cups: {' '.join(str(_) for _ in cups)}")
        break

    current_cup = cups[0]
    current_bottle = bottles[-1]

    if current_bottle > current_cup:
        wasted_water += (current_bottle - current_cup)
        cups.popleft()
        bottles.pop()

    elif current_bottle < current_cup:
        current_cup -= current_bottle
        cups[0] = current_cup
        bottles.pop()
        continue

    elif current_bottle == current_cup:
        cups.popleft()
        bottles.pop()

print(f"Wasted litters of water: {wasted_water}")


