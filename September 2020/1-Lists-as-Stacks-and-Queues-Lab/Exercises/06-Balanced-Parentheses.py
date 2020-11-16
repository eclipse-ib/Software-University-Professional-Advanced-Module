string = input()

stack = []
result = ""

if len(string) % 2 != 0:
    print("NO")
    exit()

else:
    for char in string:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        else:
            if stack[-1]+char == "()" or \
                    stack[-1] + char == "{}" or \
                    stack[-1] + char == "[]":
                stack.pop()

if len(stack) != 0:
    result = "NO"
else:
    result = "YES"
print(result)
