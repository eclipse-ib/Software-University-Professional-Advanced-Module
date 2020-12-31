import os

while True:
    commands = input().split("-")
    command = commands[0]
    if command == "End":
        break
    file_name = commands[1]

    if command == "Create":
        # new_file = open(file_name, "w")
        # new_file.close()
        with open("file_name", "w") as new_file:
            new_file.write("")
    elif command == "Add":
        content = commands[2]
        try:
            # new_file = open(file_name, "a")
            # print(content, file=new_file)
            # new_file.close()
            with open("file_name", "a") as new_file:
                print(content, file=new_file)
        except FileNotFoundError:
            with open("file_name", "w") as new_file:
                print(content, file=new_file)
            # new_file = open(file_name, "w")
            # print(content, file=new_file)
            # new_file.close()

    elif command == "Replace":
        old_string = commands[2]
        new_string = commands[3]
        try:
            new_file = open(file_name, "r")
            s = new_file.read()
            new_file.close()
            s = s.replace(old_string, new_string)
            new_file = open(file_name, "w")
            new_file.write(s)
            new_file.close()
        except FileNotFoundError:
            print(f"An error occurred")

    elif command == "Delete":
        file_path = "text.txt"
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print(f"An error occurred")
