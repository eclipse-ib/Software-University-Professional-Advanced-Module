# # Алтернативен вариант с for цикъл и апендване на елемента, който  епремахнат отляво(popleft)
# from collections import deque
#
# names = deque(input().split())
# toss = int(input())
#
# while len(names) > 1:
#     for _ in range(toss):
#         names.append(names.popleft())
#         print(f"Removed {names.pop()}")
#
# print(f"Last is {names[0]}")



# #Съкратена версия
from collections import deque

names = deque(input().split())
toss = int(input())

while len(names) > 1:
    names.rotate(-toss)
    print(f"Removed {names.pop()}")

print(f"Last is {names[0]}")