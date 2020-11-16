robots_info = input().split(";")
hours, minutes, seconds = input().split(":")
robots = []
products = []

for robot in robots_info:
    robot_name, robot_time = robot.split("-")
    robots.append([robot_name, robot_time])

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

