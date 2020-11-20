from collections import deque

water_quantity = int(input())

names = deque([])

while True:
    name = input()

    if name == "Start":
        break

    names.append(name)

while True:
    commands = input().split()

    if commands[0] == "End":
        print(f"{water_quantity} liters left")
        break

    elif commands[0] == "refill":
        added_water = int(commands[1])
        water_quantity += added_water

    else:
        person_liters = int(commands[0])
        if int(person_liters) > water_quantity:
            person = names[0]
            print(f"{person} must wait")
            names.popleft()
            continue
        print(f"{names[0]} got water")
        water_quantity -= int(person_liters)
        names.popleft()