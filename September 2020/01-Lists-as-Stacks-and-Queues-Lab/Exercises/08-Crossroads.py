from collections import deque

green_light_duration = int(input())
free_window = int(input())
no_crash_window = green_light_duration + free_window

passed_cars = 0

while True:
    command = input()
    if command == "END":
        print(f"Everyone is safe.\n{passed_cars} total cars passed the crossroads.")
        break

    elif command == "green":
        no_crash_window = green_light_duration + free_window

    else:
        car_name = command
        car = deque(car_name)

        if no_crash_window - free_window > 0:
            while no_crash_window > 0:
                if len(car) == 0:
                    passed_cars += 1
                    break
                car.popleft()
                no_crash_window -= 1
        if no_crash_window == 0 and len(car) > 0:
            print(f"A crash happened!\n{car_name} was hit at {car[0]}.")
            break
