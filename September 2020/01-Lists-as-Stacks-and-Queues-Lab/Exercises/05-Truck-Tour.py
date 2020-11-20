from collections import deque

number_of_pomps = int(input())

pumps = deque()

for n in range(number_of_pomps):
    pump = [int(_) for _ in input().split()]
    pumps.append(pump)

for i in range(number_of_pomps):
    is_valid = True
    fuel = 0

    for _ in range(number_of_pomps):
        current = pumps.popleft()
        fuel += current[0] - current[1]

        if fuel < 0:
            is_valid = False
        pumps.append(current)

    if is_valid:
        print(i)
        break

    pumps.append(pumps.popleft())