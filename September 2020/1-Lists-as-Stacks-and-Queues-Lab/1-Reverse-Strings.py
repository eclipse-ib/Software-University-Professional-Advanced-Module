# Вариант 4 / видео / съкратен
stack = list(input())

while len(stack) != 0:
    item = stack.pop()
    print(item, end="")

# # Вариант 3 / видео
# string = input()
# stack = []
# for i in string:
#     stack.append(i)
# stack = list(input())
# reversed_stack = ''
# while len(stack) != 0:
#     item = stack.pop()
#     reversed_stack += item
# print(reversed_stack)

# # Вариант 2
# string = input()
# stack = []
# for i in string:
#     stack.append(i)
#
# reversed_stack = ''
# for j in range(len(stack)):
#     reversed_stack += stack.pop()
#
# print(''.join(reversed_stack))
#
#
# # Вариант 1
# string = input()
# stack = []
# for i in string:
#     stack.append(i)
#
# reversed_stack = []
# for j in range(len(stack)):
#     reversed_stack.append(stack.pop())
#
# print(''.join(reversed_stack))