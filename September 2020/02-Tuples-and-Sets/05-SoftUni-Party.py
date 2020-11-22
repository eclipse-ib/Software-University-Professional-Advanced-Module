# Друг мой вариант с използването само на един сет
number_of_guests = int(input())
guests = set()

while True:
    guest = input()
    if guest == "END":
        break

    elif guest not in guests:
        guests.add(guest)

    elif guest in guests:
        guests.remove(guest)

print(len(guests))
print('\n'.join(sorted(guests)))


# Мой вариант с 2 сета (ненужни за условието на задачата):
# number_of_guests = int(input())
#
# vip_guests = set()
# normal_guests = set()
#
#
# while True:
#     guest = input()
#     if guest == "END":
#         break
#
#     elif guest not in vip_guests and guest[0].isdigit():
#         vip_guests.add(guest)
#
#     elif guest in vip_guests and guest[0].isdigit():
#         vip_guests.remove(guest)
#
#     elif not guest[0].isdigit() and guest not in normal_guests:
#         normal_guests.add(guest)
#
#     elif not guest[0].isdigit() and guest in normal_guests:
#         normal_guests.remove(guest)
#
# print(len(vip_guests) + len(normal_guests))
#
# for i in sorted(vip_guests):
#     print(i)
#
# for j in sorted(normal_guests):
#     print(j)


