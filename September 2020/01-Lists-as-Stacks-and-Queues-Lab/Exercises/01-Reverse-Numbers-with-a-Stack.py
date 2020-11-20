string = list(input().split())
rotated_string = []
while len(string) > 0:
    rotated_string.append(string.pop())
print(' '.join(rotated_string))