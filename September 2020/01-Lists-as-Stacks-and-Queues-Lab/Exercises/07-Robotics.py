from collections import deque

robots_info = input().split(";")

started_time = input().split(":")
hours = int(started_time[0])
minutes = int(started_time[1])
seconds = int(started_time[2])

available_robots = deque()
processing_robots = deque()
products = deque()

for robot in robots_info:
    robot_name, robot_time = robot.split("-")
    available_robots.append([robot_name, robot_time])

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while len(products) != 0:

    for _ in processing_robots:
        _[1] -= 1
        if _[1] <= 0:
            available_robots.append(_[0])
    processing_robots = [p_robot for p_robot in processing_robots if p_robot[1] > 0]

    seconds += 1

    if seconds > 59:
        minutes += 1
        seconds = 0
    if minutes > 59:
        hours += 1
        minutes = 0
    if hours == 24:
        hours = 0

    product_on_line = products.popleft()

    if not available_robots:
        products.append(product_on_line)
        continue

    if available_robots:

        current_robot = available_robots.popleft()

        print(f"{current_robot[0]} - {product_on_line} [{hours:02d}:{minutes:02d}:{seconds:02d}]")

        processing_robots.append([current_robot, int(current_robot[1])])