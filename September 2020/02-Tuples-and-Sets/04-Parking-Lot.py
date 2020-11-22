#Решение с използване на OOP:
class Parking:
    def __init__(self):
        self.__cars = set()

    def process_car(self, direction, car):
        if direction == "IN":
            self.__cars.add(car)
        elif direction == "OUT" and car in self.__cars:
            self.__cars.remove(car)

    def print_status(self):
        if self.__cars:
            print("\n".join([reg_num for reg_num in self.__cars]))
        else:
            print("Parking Lot is Empty")


parking = Parking()

n = int(input())
for _ in range(n):
    direction, reg_num = input().split(", ")
    parking.process_car(direction, reg_num)

parking.print_status()




#Още по=оптимизирано решение, при което има проверка за това дали автомобила е в паркинга,
# преди да бъде премахнат изписано с функции:
# n = int(input())
#
# parking = set()
#
#
# def get_in_parking(car_number):
#     parking.add(car_number)
#
#
# def get_out_of_parking(car_number):
#     if car_number in parking:
#         parking.remove(car_number)
#
#
# for _ in range(n):
#     direction, car_number = input().split(", ")
#     operations = {
#         "IN": get_in_parking,
#         "OUT": get_out_of_parking
#     }
#     operations[direction](car_number)
#
# if parking:
#     print("\n".join(parking))
# else:
#     print("Parking Lot is Empty")


# Оптимизирано решение без използването на condition statements в ядрото:
# n = int(input())
#
# parking = set()
#
# for _ in range(n):
#     direction, car_number = input().split(", ")
#     operations = {
#         "IN": parking.add,
#         "OUT": parking.remove
#     }
#     operations[direction](car_number)
#
# if parking:
#     print("\n".join(parking))
# else:
#     print("Parking Lot is Empty")



# Мое решение:
# n = int(input())
#
# parking = set()
#
# for _ in range(n):
#     direction, car_number = input().split(", ")
#
#     if direction == "IN":
#         parking.add(car_number)
#     else:
#         parking.remove(car_number)
#
# if parking:
#     print("\n".join(parking))
# else:
#     print("Parking Lot is Empty")